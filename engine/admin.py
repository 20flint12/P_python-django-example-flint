from django.contrib import admin

# Register your models here.
from engine import models
from engine.models import MoonZodiac, Factor


class ZodiacContentInline(admin.TabularInline):
    model = models.ZodiacContent
    extra = 1


class MoonZodiacAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'pk',
        'zodiac',
    )
    list_display_links = (
        'zodiac',
    )
    inlines = (ZodiacContentInline,)


class FactorAdmin(admin.ModelAdmin):
    list_display = (
        'moon_zodiac', 'pk',
        'serves_hot_dogs',
    )






admin.site.register(MoonZodiac, MoonZodiacAdmin)
admin.site.register(Factor, FactorAdmin)
