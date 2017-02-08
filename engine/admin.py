from django.contrib import admin

# Register your models here.
from engine import models
from engine.models import MoonZodiac, SummaryFactor, MoonDay, Observer, MoonDayContent


class MoonZodiacContentInline(admin.TabularInline):
    model = models.MoonZodiacContent
    extra = 1


class MoonZodiacAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'summaryfactor',
        'title',
        'zodiac_choice',
    )
    # list_display_links = (
    #     'zodiac',
    # )
    inlines = (MoonZodiacContentInline,)


class MoonDayContentInline(admin.TabularInline):
    model = models.MoonDayContent
    extra = 1


class MoonDayContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'moonday',
        'title',
        'source',
        'symbol',
        'image',
    )


class MoonDayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'summaryfactor',
        'title',
        'quality',
        'day_choice',
    )
    # list_display_links = (
    #     'zodiac',
    # )
    inlines = (MoonDayContentInline,)


class SummaryFactorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'serves_pizza',
    )


class ObserverAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'userprofile',
        'created_at',
        'updated_at',
        'title',
        # 'text',
        'is_active',
        'timezone_name',
        'dst',
        'latitude',
        'longitude',
    )


admin.site.register(MoonZodiac, MoonZodiacAdmin)
admin.site.register(MoonDayContent, MoonDayContentAdmin)
admin.site.register(MoonDay, MoonDayAdmin)
admin.site.register(SummaryFactor, SummaryFactorAdmin)
admin.site.register(Observer, ObserverAdmin)

