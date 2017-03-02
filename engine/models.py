from __future__ import unicode_literals

import sys
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from astrouser.models import UserProfile

import engine.astro_routines.geo_place as geo

'''
SummaryFactor(zodiac,moonday)
    MoonZodiac(descr, picture)                  summaryfactor   <==  related_mzodiac
        MoonZodiacContent(descr,source,image)   moonzodiac      <==  related_mzcontent
    MoonDay(descr, picture)                     summaryfactor   <==  related_mday
        MoonDayContent(descr,source,image)      moonday         <==  related_mdcontent

Observer
    userprofile  <==  related_observer


python manage.py dumpdata \
astrouser.User astrouser.UserProfile \
engine.SummaryFactor \
engine.MoonZodiac engine.MoonZodiacContent \
engine.MoonDay engine.MoonDayContent \
engine.Observer > astrofactor.json

'''


class SummaryFactor(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    marked_at = models.DateTimeField(blank=True, default=None, null=True)

    title = models.CharField(max_length=50, default='')
    special_case = models.BooleanField(default=False)

    moon_lng = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], null=True, blank=True, default=None)
    moon_lat = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(180.0)], null=True, blank=True, default=None)
    moon_phase = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], null=True, blank=True, default=None)

    def __str__(self):
        return "{} special:{}".format(self.title, self.special_case)


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
    summaryfactor = models.ForeignKey(SummaryFactor, related_name="related_mzodiac", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    zodiac_choice = models.PositiveSmallIntegerField(blank=False, null=False, choices=MOON_ZODIACS)

    def __str__(self):
        return "id:{} {} of {}".format(self.id, self.zodiac_choice, self.title)


class MoonZodiacContent(models.Model):

    moonzodiac = models.ForeignKey(MoonZodiac, related_name="related_mzcontent", on_delete=models.CASCADE, blank=True, null=True)

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
    summaryfactor = models.ForeignKey(SummaryFactor, related_name="related_mday", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=50)
    quality = models.CharField(max_length=250, default='')  # the quality of the day
    day_choice = models.PositiveSmallIntegerField(blank=False, null=False, choices=MOON_DAYS)

    def __str__(self):
        return "[{}-й л.д.] {}".format(self.day_choice, self.title)


class MoonDayContent(models.Model):

    moonday = models.ForeignKey(MoonDay, related_name="related_mdcontent", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=250, default='')
    symbol = models.CharField(max_length=250, default='', blank=True, null=True)
    description = models.TextField()
    image = models.FileField(upload_to='media/moonday_imgs/%Y/%m/%d/', blank=True, null=True)
    source = models.URLField(max_length=250, default='')

    def __str__(self):
        return "[{}] Symbol: {}".format(self.title, self.symbol)


class Observer(models.Model):

    userprofile = models.ForeignKey(UserProfile, related_name="related_observer", on_delete=models.CASCADE, blank=True, null=True)

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
        return "[{}] Observer: {} lat:{} lon:{}".format(self.id, self.title, self.latitude, self.longitude)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('edit_observer', args=[str(self.id)])

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

        return super(Observer, self).save(force_insert, force_update, using, update_fields)

