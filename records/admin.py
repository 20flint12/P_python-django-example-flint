#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.contrib import admin
from models import Publisher, Author, Book, RecNews, WeatherData


# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'pk',
        'address',
        'city',
    )
    # date_hierarchy = 'created_at'
    # actions = [freeze_modules, publish_modules]


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author)
admin.site.register(Book)

admin.site.register(RecNews)
admin.site.register(WeatherData)
