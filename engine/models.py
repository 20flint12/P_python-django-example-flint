#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

'''
Factor(zodiac,moonday)
    MoonZodiac(descr, picture)
        ZodiacContent(descr,source,image)
        ZodiacContent(descr,source,image)
    MoonDay(descr, picture)
        DayContent(descr,source,image)
        DayContent(descr,source,image)
        DayContent(descr,source,image)
'''


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

    name = models.CharField(max_length=50)
    zodiac = models.PositiveSmallIntegerField(blank=False, null=False, choices=MOON_ZODIACS)

    def __str__(self):
        return "{} of {}".format(self.name, self.zodiac)


class Factor(models.Model):
    #TODO OneToOneField
    moon_zodiac = models.OneToOneField(MoonZodiac, on_delete=models.CASCADE, primary_key=True, )
    # moon_zodiac = models.OneToOneField(MoonZodiac, on_delete=models.CASCADE, primary_key=True, )

    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "{} of {}".format(self.moon_zodiac, self.serves_hot_dogs)


class ZodiacContent(models.Model):
    zodiac = models.ForeignKey(MoonZodiac, related_name="content_zodiac", blank=True, null=True)

    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.FileField(upload_to='media/zodiac_imgs/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return "[{}] Content: {}".format(self.id, self.title)
