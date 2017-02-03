import json
from django.urls import reverse_lazy
from django.utils.dateparse import parse_datetime
from django.views.generic import View, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from engine.astro_routines import geo_place
from engine.astro_routines import sun_rise_sett
from engine.forms import PlaceForm, ToDoForm
from engine.mixin import PlacePermissionMixin
from engine.models import Place


class NewPlaceView(LoginRequiredMixin, CreateView):
    template_name = 'engine/new_place.html'
    form_class = PlaceForm

    # # add the request to the kwargs
    # def get_form_kwargs(self):
    #     kwargs = super(NewPlaceView, self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs

    def get_success_url(self):
        return reverse_lazy('new_place',
                            kwargs={'place_id': self.object.id})

    # def form_valid(self, form):
    #     form.instance.user_id = self.request.user.id
    #     form.instance.edit_version = True
    #     return super(NewStudyModuleView, self).form_valid(form)


class PlaceEditView(LoginRequiredMixin, UpdateView):
    template_name = 'engine/edit_place.html'
    queryset = Place.objects
    form_class = PlaceForm

    def get_object(self, **kwargs):
        place = Place.objects.get(pk=self.kwargs['place_id'])
        return place

    # def post(self, request, *args, **kwargs):
    #
    #     return super(PlaceEditView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        place_id = self.kwargs['place_id']
        return reverse_lazy('edit_place', kwargs={'place_id': place_id})


class Observer:
    """
    Common base class for observer
    """
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Observer.empCount += 1


class MomentView(LoginRequiredMixin, FormView):

    template_name = 'engine/edit_time.html'
    form_class = ToDoForm

    def get_success_url(self):
        place_id = self.kwargs['place_id']
        return reverse_lazy('edit_moment', kwargs={'place_id': place_id})

    def get_context_data(self, **kwargs):
        context = super(MomentView, self).get_context_data(**kwargs)

        context['place_id'] = self.kwargs['place_id']

        if 'unaware_loc' in self.request.session and self.request.session['unaware_loc']:
            unaware_loc_str = self.request.session['unaware_loc']
            unaware_loc = parse_datetime(unaware_loc_str)
            context['unaware_loc'] = str(unaware_loc)

            place = Place.objects.get(pk=self.kwargs['place_id'])
            tz = place.timezone_name
            aware_loc = geo_place.set_tz_to_unaware_time(tz, unaware_loc)
            context['aware_loc'] = str(aware_loc)

            aware_utc = geo_place.aware_time_to_utc(aware_loc)
            context['aware_utc'] = str(aware_utc)

            sun_rs = sun_rise_sett.get_sun_rise_sett(aware_utc, (22, 33))
            context['sun_rise_sett'] = json.dumps(sun_rs)

        return context

    def post(self, request, *args, **kwargs):

        # TODO Calculate ephem
        # dp2 = request.POST['dp2']
        # unaware_loc = request.POST['dp3']
        # result = request.POST['result']

        request.session['unaware_loc'] = request.POST.get('unaware_local')

        return super(MomentView, self).post(request, *args, **kwargs)
