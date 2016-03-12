#!/usr/bin/env python
# -*- coding: utf-8 -*-



from django.shortcuts import render_to_response
from django.http import HttpResponse


import datetime
import ephem

import os
import sys


import scrapes.scrape_data2 as scr2
import scrapes.scrape_data3 as scr




def current_datetime(request):
    # now = datetime.datetime.now()

    s_out = ""
    for path in sys.path:
        # print path
        s_out += path + "\n"

    return render_to_response('Current_date_time.html', {'current_date': s_out})





def scrape_data_req(request):
    now = datetime.datetime.now()
    # cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # news = scr.get_news()
    news = scr2.get_temperature()
    # print unicode(news)
    return render_to_response('scrape_data.html',
                              {'current_site':now,
                               'data_context':news})





def display_meta(request):
    values = request.META.items()

    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))

    return HttpResponse('<table>%s</table>' % '\n'.join(html))




def main_index(request):

    # return HttpResponse('index.html')
    return render_to_response('index.html',
                                {'#isCurrentDay':1})




# file charts.py

def my_simple(request):

    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    # print "!" * 100

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=4)
    for i in range(30):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()

    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response











if __name__ == '__main__':

    # print locals()

    for path in sys.path:
        print path




    # sys.path.pop(0)

    # sys.path.append("/home/flint/Projects/Py_projects/P_virtualenv/ENV_H/P_python-django-example-flint/mysite")


    # print "========================================"
    # for path in sys.path:
    #     print path


    # print sys.path
    # print scr


