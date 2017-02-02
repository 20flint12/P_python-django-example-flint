from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from engine.models import Place


class PlacePermissionMixin(object):
    """
    * Checks whether the user is the author of the module and whether the page is
      belong to the module, if not redirects to 'no access' view.
    * Sets 'mymodule', 'mypage' properties to the view.
    """

    str_out = "3333333333333333333"

    def dispatch(self, request, *args, **kwargs):
        print("place permission")

        if 'place_id' in kwargs:
            try:
                place = Place.objects.get(pk=kwargs['place_id'])
                self.current_place = place

                # if request.user.id == place.user_id:
                #     pass
                # else:
                #     return HttpResponseRedirect(reverse_lazy('no_access'))

            except Place.DoesNotExist:
                return HttpResponseRedirect(reverse_lazy('no_access'))

        return super(PlacePermissionMixin, self).dispatch(request, *args, **kwargs)
