#!/usr/bin/env python
# -*- coding: utf-8 -*-



from django.contrib import admin




# Register your models here.


from records.models import Publisher, Author, Book, RecNews, WeatherData

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)

admin.site.register(RecNews)
admin.site.register(WeatherData)