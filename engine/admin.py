from django.contrib import admin

# Register your models here.
from engine.models import MoonZodiac, Factor


class MoonZodiacAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'pk',
        'zodiac',
    )


class FactorAdmin(admin.ModelAdmin):
    list_display = (
        'moon_zodiac', 'pk',
        'serves_hot_dogs',
    )


admin.site.register(MoonZodiac, MoonZodiacAdmin)
admin.site.register(Factor, FactorAdmin)
