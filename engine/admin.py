from django.contrib import admin

# Register your models here.
from engine import models
from engine.models import MoonZodiac, SummaryFactor, MoonDay, Observer, MoonDayContent, Sensation


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
        'marked_at',
        'title',
        'special_case',
        'moon_lng',
        'moon_lat',
        'moon_phase',
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


class SensationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user_profile',
        'created_at',
        'began_at',
        'duration',
        'mark_day_as_a_whole',
        'mark_body',
        'mark_emotions',
        'mark_intelligence',
        'details',
    )


admin.site.register(MoonZodiac, MoonZodiacAdmin)
admin.site.register(MoonDayContent, MoonDayContentAdmin)
admin.site.register(MoonDay, MoonDayAdmin)
admin.site.register(SummaryFactor, SummaryFactorAdmin)
admin.site.register(Observer, ObserverAdmin)
admin.site.register(Sensation, SensationAdmin)

