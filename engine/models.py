from __future__ import unicode_literals

from django.db import models


'''
SummaryFactor(zodiac,moonday)
    MoonZodiac(descr, picture)                  MZodiac     <== factor_mzodiac
        MoonZodiacContent(descr,source,image)   MZContent   <== mzodiac_content
    MoonDay(descr, picture)                     MDay        <== factor_mday
        MoonDayContent(descr,source,image)      MDContent   <== mday_content
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
    mzodiac = models.ForeignKey(SummaryFactor, related_name="factor_mzodiac", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    zodiac_choice = models.PositiveSmallIntegerField(blank=False, null=False, choices=MOON_ZODIACS)

    def __str__(self):
        return "id:{} {} of {}".format(self.id, self.zodiac_choice, self.title)


class MoonZodiacContent(models.Model):

    mzcontent = models.ForeignKey(MoonZodiac, related_name="mzodiac_content", on_delete=models.CASCADE, blank=True, null=True)

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
    )

    mday = models.ForeignKey(SummaryFactor, related_name="factor_mday", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=50)
    day_choice = models.PositiveSmallIntegerField(blank=False, null=False, choices=MOON_DAYS)

    def __str__(self):
        return "{} of {}".format(self.title, self.day_choice)


class MoonDayContent(models.Model):

    mdcontent = models.ForeignKey(MoonDay, related_name="mday_content", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.FileField(upload_to='media/zodiac_imgs/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return "[{}] Content: {}".format(self.title, self.text)
