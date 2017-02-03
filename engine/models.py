from __future__ import unicode_literals

import sys
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from astrouser.models import UserProfile

import engine.astro_routines.geo_place as geo

'''
SummaryFactor(zodiac,moonday)
    MoonZodiac(descr, picture)                  mzodiac     <==  related_mzodiac
        MoonZodiacContent(descr,source,image)   mzcontent   <==  related_mzcontent
    MoonDay(descr, picture)                     mday        <==  related_mday
        MoonDayContent(descr,source,image)      mdcontent   <==  related_mdcontent
'''


class SummaryFactor(models.Model):

    marked_at = models.DateTimeField(blank=True, default=None, null=True)

    title = models.CharField(max_length=50, default='')
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "{} of {}".format(self.title, self.serves_pizza)


class MoonZodiac(models.Model):

    MOON_ZODIACS = (
        (1, 'Овен'),
        (2, 'Телец'),
        (3, 'Близнецы'),
        (4, 'Рак'),
        (5, 'Лев'),
        (6, 'Дева'),
        (7, 'Весы'),
        (8, 'Скорпион'),
        (9, 'Стрелец'),
        (10, 'Козерог'),
        (11, 'Водолей'),
        (12, 'Рыбы'),
    )
    mzodiac = models.ForeignKey(SummaryFactor, related_name="related_mzodiac", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    zodiac_choice = models.PositiveSmallIntegerField(blank=False, null=False, choices=MOON_ZODIACS)

    def __str__(self):
        return "id:{} {} of {}".format(self.id, self.zodiac_choice, self.title)


class MoonZodiacContent(models.Model):

    mzcontent = models.ForeignKey(MoonZodiac, related_name="related_mzcontent", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.FileField(upload_to='media/zodiac_imgs/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return "[{}] Content: {}".format(self.id, self.title)


class MoonDay(models.Model):

    MOON_DAYS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
    )
    mday = models.ForeignKey(SummaryFactor, related_name="related_mday", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=50)
    day_choice = models.PositiveSmallIntegerField(blank=False, null=False, choices=MOON_DAYS)

    def __str__(self):
        return "[{}] {}".format(self.day_choice, self.title)


class MoonDayContent(models.Model):

    mdcontent = models.ForeignKey(MoonDay, related_name="related_mdcontent", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.FileField(upload_to='media/zodiac_imgs/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return "[{}] Content: {}".format(self.title, self.text)


class Place(models.Model):

    profile = models.ForeignKey(UserProfile, related_name="related_profile", on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)

    title = models.CharField(max_length=250)
    text = models.TextField()

    longitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], null=True, blank=True, default=None)
    latitude = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(180.0)], null=True, blank=True, default=None)

    timezone_name = models.CharField(max_length=250, null=True, blank=True, default=None)     # "Europe/Zaporozhye"
    dst = models.BooleanField(blank=True, default=False)

    # Additional parameters
    pressure = models.FloatField(null=True, blank=True, default=1010.)   # millibar
    temperature = models.FloatField(null=True, blank=True, default=25.)  # deg. Celcius
    horizon = models.FloatField(null=True, blank=True, default=0.)
    elevation = models.FloatField(null=True, blank=True, default=3.)     # meters

    def __str__(self):
        return "[{}] Place: {} lat:{} lon:{}".format(self.id, self.title, self.latitude, self.longitude)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('edit_place', args=[str(self.id)])

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        pass
        print('asdasd', self.title)

        place_name = self.title     # 'Boston'
        coord = None

        # Update from Google ##################################################
        try:
            coord = geo.get_place_coord(place_name)
            self.latitude = coord[0]
            self.longitude = coord[1]
        except:
            str_res = "Unexpected error:" + str(sys.exc_info()[0]) + str(sys.exc_info()[1])
            print(str_res)
        print(place_name, coord)

        # pip install timezonefinder
        def find_timezone(lat, lng):

            from timezonefinder import TimezoneFinder

            tf = TimezoneFinder()
            try:
                timezone_name = tf.timezone_at(lng=lng, lat=lat)
                if timezone_name is None:
                    timezone_name = tf.closest_timezone_at(lng=lng, lat=lat)
                    # maybe even increase the search radius when it is still None

                # ... do something with timezone_name ...
                return timezone_name

            except ValueError:
                print('Oops!')
                # the coordinates were out of bounds
                # {handle error}

        # tz_name = geo.get_tz_name(coord)

        tz_name = find_timezone(coord[0], coord[1])
        self.timezone_name = tz_name
        print("tz_name=", tz_name)

        return super(Place, self).save(force_insert, force_update, using, update_fields)

