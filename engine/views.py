import json
from django.urls import reverse_lazy
from django.utils.dateparse import parse_datetime
from django.views.generic import View, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from engine.astro_routines import geo_place
from engine.astro_routines import moon_day
from engine.astro_routines import sun_rise_sett
from engine.astro_routines import zodiac_phase
from engine.forms import ObserverForm, ToDoForm
from engine.mixin import ObserverPermissionMixin
from engine.models import Observer, MoonDay


class NewObserverView(LoginRequiredMixin, CreateView):
    template_name = 'engine/new_observer.html'
    form_class = ObserverForm

    def get_success_url(self):
        return reverse_lazy('edit_observer',
                            kwargs={'place_id': self.object.id})


class ObserverEditView(LoginRequiredMixin, UpdateView):
    template_name = 'engine/edit_observer.html'
    queryset = Observer.objects
    form_class = ObserverForm

    def get_object(self, **kwargs):
        place = Observer.objects.get(pk=self.kwargs['place_id'])
        return place

    # def post(self, request, *args, **kwargs):
    #
    #     return super(PlaceEditView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        place_id = self.kwargs['place_id']
        return reverse_lazy('edit_observer', kwargs={'place_id': place_id})


class MomentView(LoginRequiredMixin, FormView):

    template_name = 'engine/edit_moment.html'
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

            place = Observer.objects.get(pk=self.kwargs['place_id'])
            tz = place.timezone_name
            aware_loc = geo_place.set_tz_to_unaware_time(tz, unaware_loc)
            context['aware_loc'] = str(aware_loc)

            aware_utc = geo_place.aware_time_to_utc(aware_loc)
            context['aware_utc'] = str(aware_utc)

            sun_rs = sun_rise_sett.get_sun_rise_sett(aware_utc, (22, 33))
            context['sun_rise_sett'] = json.dumps(sun_rs)

            mn_ph_res = moon_day.get_moon_phase(aware_utc)
            context['mn_ph_res'] = json.dumps(mn_ph_res)

            tp_md_ext, ctx2 = moon_day.get_moon_day(aware_utc, (22, 33))
            context['tp_md_ext'] = json.dumps(tp_md_ext)
            md_choice = tp_md_ext['moon_day']
            m_day = MoonDay.objects.filter(day_choice=md_choice).first()
            if m_day:
                # cnt = m_day.mdcontent_set.filter().first()
                cnt = m_day.related_mdcontent.filter().first()
                print(m_day, 'cnt=', cnt)

        return context

    def post(self, request, *args, **kwargs):

        # TODO Calculate ephem
        # dp2 = request.POST['dp2']
        # unaware_loc = request.POST['dp3']
        # result = request.POST['result']

        request.session['unaware_loc'] = request.POST.get('unaware_local')

        return super(MomentView, self).post(request, *args, **kwargs)

