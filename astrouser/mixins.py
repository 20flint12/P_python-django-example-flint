from __future__ import print_function
from __future__ import print_function
from django.http import HttpResponseRedirect, HttpResponse


class AjaxHandlerMixin(object):
    """Pass ajax requests to handlers determined by 'action' parameter"""

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if 'action' in request.POST and hasattr(self, request.POST['action']):
                handler = getattr(self, request.POST['action'])
                return handler(request)
            else:
                return HttpResponse('Action not provided or incorrect', status=400)
        else:
            return HttpResponse('Bad request', status=400)
