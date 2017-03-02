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

import datetime
import ephem


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

            coord = (place.latitude, place.longitude)
            sun_rs = sun_rise_sett.get_sun_rise_sett(aware_utc, coord)
            context['sun_rise_sett'] = json.dumps(sun_rs)

            mn_ph_res = moon_day.get_moon_phase(aware_utc)
            context['mn_ph_res'] = json.dumps(mn_ph_res)

            tp_md_ext, ctx2 = moon_day.get_moon_day(aware_utc, coord)
            context['tp_md_ext'] = json.dumps(tp_md_ext)
            md_choice = tp_md_ext['moon_day']
            m_day = MoonDay.objects.filter(day_choice=md_choice).first()
            if m_day:
                # cnt = m_day.mdcontent_set.filter().first()
                cnt = m_day.related_mdcontent.filter()
                print(m_day, 'cnt=', cnt)

            # Summary data
            summary = self.summary_info(aware_utc, coord, tz)
            context['summary_data'] = summary


        return context

    def post(self, request, *args, **kwargs):

        # TODO Calculate ephem
        # dp2 = request.POST['dp2']
        # unaware_loc = request.POST['dp3']
        # result = request.POST['result']

        request.session['unaware_loc'] = request.POST.get('unaware_local')

        return super(MomentView, self).post(request, *args, **kwargs)

    def summary_info(self, aware_utc, coord, tz_name):
        str_out = ""
        dtformat = "%Y-%m-%d %H:%M:%S %z"
        dtsunformat = "%H:%M:%S"
        dtmoonformat = "%m-%d %H:%M:%S"
        for d in range(0, 95):
            cur_date_loc = aware_utc+datetime.timedelta(days=d)
            # str_out += 'cur_date_loc=' + str(cur_date_loc)

            cur_noon_loc = datetime.datetime(cur_date_loc.year, cur_date_loc.month, cur_date_loc.day, 12, 0, 0)
            # str_out += "cur_noon_loc=" + str(cur_noon_loc) + " "
            # -------------------------------------------------------------------------

            aware_loc = geo_place.set_tz_to_unaware_time(tz_name, cur_noon_loc)
            str_out += "local=" + str(aware_loc.strftime(dtformat)) + ', '
            # -------------------------------------------------------------------------

            cur_date_utc = geo_place.aware_time_to_utc(aware_loc)
            # str_out += "utc=" + str(cur_date_utc.strftime(dtformat)) + ', '
            # -------------------------------------------------------------------------

            summary = sun_rise_sett.get_sun_rise_sett(cur_date_utc, coord)
            str_out += 's_r/s=' + str(geo_place.utc_to_loc_time(tz_name, ephem.Date(summary["day_rise"]).datetime()).strftime(dtsunformat)) + ', '
            str_out += str(geo_place.utc_to_loc_time(tz_name, ephem.Date(summary["day_sett"]).datetime()).strftime(dtsunformat)) + ', '
            # str_out += "day_rise=", summary['day_rise'].strftime(dtformat)
            # -------------------------------------------------------------------------

            mp_result = moon_day.get_moon_phase(cur_date_utc)
            str_out += 'ph=' + mp_result['next'] + ', '
            phase_time = mp_result[mp_result['next'] + '_utc']
            str_out += 'ph_t=' + str(geo_place.utc_to_loc_time(tz_name, ephem.Date(phase_time).datetime()).strftime(dtformat)) + ', '
            # -------------------------------------------------------------------------

            tp_md_ext, ctx2 = moon_day.get_moon_day(cur_date_utc, coord)
            str_out += "md={:2d}".format(tp_md_ext['moon_day']) + ', '
            str_out += 'mrise=' + str(geo_place.utc_to_loc_time(tz_name, ephem.Date(tp_md_ext['day_rise']).datetime()).strftime(dtmoonformat)) + ', '
            str_out += 'msett=' + str(geo_place.utc_to_loc_time(tz_name, ephem.Date(tp_md_ext['day_sett']).datetime()).strftime(dtmoonformat)) + ', '
            # -------------------------------------------------------------------------

            body = ephem.Sun(cur_date_utc)
            ecl_dict_ext = zodiac_phase.get_zodiac(cur_date_utc, body)
            str_out += "sz={}".format(ecl_dict_ext['zod_lat']) + ', '

            body = ephem.Moon(cur_date_utc)
            ecl_dict_ext = zodiac_phase.get_zodiac(cur_date_utc, body)
            str_out += "mz={}".format(ecl_dict_ext['zod_lat']) + ', '
            # =========================================================================

            str_out += "\n"

        print("d=", d, "summary=", summary, str_out)

        return str_out

