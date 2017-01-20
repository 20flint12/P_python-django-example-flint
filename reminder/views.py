import sys

import datetime
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView

import engine.astro_routines.moon_day as md

import engine.astro_routines.geo_place as geo
import engine.astro_routines.geo_preload as geopr

import grabber.scrapes.scrape_data3 as scr
import grabber.scrapes.scrape_data2 as scr2


class ReminderView(View):
    template_name = 'reminder/no_access.html'

    def get_context_data(self, **kwargs):
        context = super(ReminderView, self).get_context_data(**kwargs)
        return context


def current_datetime(request):
    # now = datetime.datetime.now()

    s_out = ""
    for path in sys.path:
        # print path
        s_out += path + "\n"

    return render_to_response('reminder/Current_date_time.html', {'current_date': s_out})


def scrape_data_req(request):
    now = datetime.datetime.now()
    # cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # news = scr.get_news()
    news = scr2.get_temperature()
    # print unicode(news)
    return render_to_response('reminder/scrape_data.html',
                              {'current_site': now,
                               'data_context': news})


def astro_req(request):

    time_loc = datetime.datetime.now()

    # ctx = epph.sun_rise()
    ctx = "" #epph.moon_rise_set()

    # cur_date_utc = ephem.now()  # current UTC date and time
    #
    # coord, tz_name = md.set_tz("Kharkiv")
    # tp, ctx2 = md.get_phase_on_current_day(cur_date_utc, coord)

    # cur_place = "Boston"
    cur_place = "Kharkiv"
    tz_name, coord = geopr.set_tz(cur_place)
    # print "cur_place=", cur_place, coord, tz_name

    # # Calculate utc date on local noon for selected place ###############
    format = "%Y-%m-%d %H:%M:%S %z"
    ###########################################################################
    cur_date_loc = datetime.datetime.today()
    # print "cur_date_loc=", cur_date_loc.strftime(format)

    # Calculate utc date on local noon for selected place #####################
    cur_noon_loc = datetime.datetime(cur_date_loc.year, cur_date_loc.month, cur_date_loc.day, 12, 0, 0)
    # print "cur_noon_loc=", cur_noon_loc

    # -------------------------------------------------------------------------
    aware_loc = geo.set_tz_to_unaware_time(tz_name, cur_noon_loc)
    # print "aware_loc=", aware_loc.strftime(format)
    cur_date_utc = geo.aware_time_to_utc(aware_loc)
    print("cur_date_utc=", cur_date_utc.strftime(format))

    tp, ctx2 = md.get_moon_day(cur_date_utc, coord)

    ctx += "\n" + ctx2
    print(ctx)

    return render_to_response('reminder/astro_data.html',
                              {'current_site': str(time_loc) + " " + cur_place,
                               'data_context': ctx})


def display_meta(request):
    values = request.META.items()

    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))

    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def main_index(request):

    # return HttpResponse('index.html')
    return render_to_response('reminder/index.html', {'#isCurrentDay': 1})


def my_simple(request):

    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    # print "!" * 100

    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=4)
    for i in range(30):
        x.append(now)
        now += delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()

    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


