#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models
from django.utils import timezone


class Publisher(models.Model):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title


class RecNews(models.Model):
    news_date = models.DateField()
    news_contents = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.news_date, self.news_contents)


class WeatherData(models.Model):

    grabbed_at = models.DateTimeField(default=timezone.now())

    check_timestamp = models.CharField(max_length=5)
    temperature_air = models.FloatField()
    temperature_com = models.IntegerField()
    temperature_dew = models.IntegerField()
    temperature_hum = models.IntegerField()
    pressure_sea = models.IntegerField()
    pressure_stn = models.IntegerField()

    def __unicode__(self):
        return u'{:s} on:{:s} temperature_air:{:2.0f} ' \
               u'{:d} {:d} {:d} ' \
               u'pressure_sea:{:d} ' \
               u'pressure_stn:{:d}'.format(str(self.weather_datetime), self.check_time,
                                           self.temperature_air, self.temperature_com,
                                           self.temperature_dew, self.temperature_hum,
                                           self.pressure_sea, self.pressure_stn)


class SpaceWeatherData(models.Model):
    grabbed_at = models.DateTimeField(default=timezone.now())

    # Mid - latitudes
    activity_level = models.CharField(max_length=50)
    p_00_24_hr = models.IntegerField()
    p_24_48_hr = models.IntegerField()
