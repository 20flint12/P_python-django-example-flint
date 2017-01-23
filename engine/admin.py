from django.contrib import admin

# Register your models here.
from engine import models
from engine.models import MoonZodiac, SummaryFactor


class ZodiacContentInline(admin.TabularInline):
    model = models.ZodiacContent
    extra = 1


class MoonZodiacAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'zodiac',
    )
    list_display_links = (
        'zodiac',
    )
    inlines = (ZodiacContentInline,)


class SummaryFactorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'serves_pizza',
    )


admin.site.register(MoonZodiac, MoonZodiacAdmin)
admin.site.register(SummaryFactor, SummaryFactorAdmin)
