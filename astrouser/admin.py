from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from astrouser.models import User, update_member, UserProfile
import logging
from django.conf import settings


logger = logging.getLogger(__name__)


class AstroFactorAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('AstroFactor admin')

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('AstroFactor administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('AstroFactor site administration')


def push_to_mailchimp(modeladmin, request, queryset):
    merge_field = '*|FNAME|*'
    errors = 0
    pushed = 0
    for user in queryset:
        print(user.email)
        try:
            update_member(user)
            pushed += 1
        except Exception as e:
            logger.error(e)
            errors += 1
            if settings.DEBUG:
                raise
    modeladmin.message_user(request, "%s user emails successfully pushed to MailChimp. %s errors." % (pushed, errors))


push_to_mailchimp.short_description = "Push selected user emails to MailChimp"


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'email',
        'date_joined',
        'last_login',
    )
    exclude = ('password',)
    actions = [push_to_mailchimp]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'account',
        'user_name',
        'user_surname',
    )


admin.site = AstroFactorAdminSite()
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
