import sys

import datetime
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView


import grabber.scrapes.scrape_data3 as scr


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
    news = scr.get_news()
    # news = scr2.get_temperature()
    # print unicode(news)
    return render_to_response('reminder/scrape_data.html',
                              {'current_site': now,
                               'data_context': news})


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


