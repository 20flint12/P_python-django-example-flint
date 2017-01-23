#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


'''
Factor(zodiac,moonday)
    MoonZodiac(descr, picture)              MZodiac     === factor_mzodiac
        ZodiacContent(descr,source,image)   MZContent   === mzodiac_content
    MoonDay(descr, picture)                 MDay        === factor_mday
        DayContent(descr,source,image)      MDContent   === mday_content
'''


class SummaryFactor(models.Model):

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

    moon_zodiac = models.ForeignKey(SummaryFactor, related_name="factor_zodiac", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=50)
    zodiac = models.PositiveSmallIntegerField(blank=False, null=False, choices=MOON_ZODIACS)

    def __str__(self):
        return "{} of {}".format(self.title, self.zodiac)


class ZodiacContent(models.Model):

    zodiac_content = models.ForeignKey(MoonZodiac, related_name="content_zodiac", on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.FileField(upload_to='media/zodiac_imgs/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return "[{}] Content: {}".format(self.title, self.text)
