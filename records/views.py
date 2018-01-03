#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import datetime
from datetime import datetime

from django.utils import timezone
from django.views.generic import TemplateView

import grabber.scrapes.scrape_data2 as scr2
from django.http import HttpResponse
from django.shortcuts import render_to_response

import grabber.scrapes.scrape_data3 as scr3
import grabber.scrapes.scrape_solar_activity as spaceweather
from records.models import Book, SpaceWeatherData
from records.models import RecNews
from records.models import WeatherData


def search_form(request):

    # # from records.models import Publisher
    # p1 = Publisher(name='Apress2', address='2855 Telegraph Avenue',
    #     city='Berkeley', state_province='CA', country='U.S.A,',
    #     website='http://www.apress.com/')
    # p1.save()
    # p2 = Publisher(name="0'Reilly2", address='10 Fawcett St.',
    #     city='Cambridge', state_province='MA', country='U.S.A.',
    #     website='http://www.oreilly.com/')
    # p2.save()

    return render_to_response('records_search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You searched: %r' % request.GET['q']
    else:
        message = 'Blank form'
    return HttpResponse(message)


def search2(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        # books = Book.objects.filter(title__icontains=q)
        # books = Publisher.objects.all()
        books = Book.objects.all()
        # books = Publisher.objects.all()
        print(books)
        return render_to_response('records_search_results.html',
            {'books': books, 'query': q})
    else:
        # return HttpResponse('Enter new req')
        return render_to_response('records_search_form.html', {'error': True})


def news(request):

    # dt = datetime.today()
    dt = timezone.now()
    # str_date_stamp = dt.strftime('%YYYY-%MM-%DD')

    ctx = scr3.get_news()
    if ctx:
        n1 = RecNews(news_date=dt, news_contents=ctx)
        n1.save()

    print("+" * 100)    #

    # ustring = unicode(read_string, encoding=...)
    n1 = RecNews(news_date=dt, news_contents=ctx)
    n1.save()

    books = RecNews.objects.all()
    return render_to_response('news_search_results.html',
                              {'books': books})


def weather(request):

    weather_collect()

    wdata = WeatherData.objects.all()
    # print wdata
    return render_to_response('news_search_results.html',
        {'books': wdata})


def weather_collect():

    # dt = datetime.today()
    dt = timezone.now()

    ctx = scr2.parse_temperature(scr2.get_temperature())
    # ctx = [u'20:00', 23, 25, 10, 44, 768, 754]
    print("weather-!-" * 5, ctx)

    if ctx:
        w = WeatherData(grabbed_at=dt,
                        check_timestamp=ctx[0],
                        temperature_air=ctx[1],
                        temperature_com=ctx[2],
                        temperature_dew=ctx[3],
                        temperature_hum=ctx[4],
                        pressure_sea=ctx[5],
                        pressure_stn=ctx[6])
        w.save()

    sctx = spaceweather.get_solar_activity()
    print("weather-!-" * 5, sctx)
    if sctx:
        sw = SpaceWeatherData(grabbed_at=dt,
                              activity_level=sctx[0][0],
                              p_00_24_hr=sctx[0][1],
                              p_24_48_hr=sctx[0][2])
        sw.save()

    print("+=!d" * 40)


def static_image(request):
    """ Simply return a static image as a png """

    # image_path = "/home/flint/Pictures/Screenshot at 2017-01-09 13-21-19.png"
    image_path = "engine/static/engine/images/images (1).jpg"

    image_data = open(image_path, "rb").read()
    return HttpResponse(image_data, content_type="image/jpg")


def weather_graph(num="1000"):

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    print(".'" * 20, "weather_chart", ".'" * 20)

    # *************************************************************************
    fig = Figure(figsize=(20, 10), dpi=80, facecolor='g', edgecolor='k')
    # ax1 = fig.add_subplot(211)
    # ax2 = fig.add_subplot(212)
    # ax1=fig.subplots_adjust(bottom=0.2)

    textsize = 9
    left, width = 0.1, 0.8
    rect1 = [left, 0.7, width, 0.2]
    rect2 = [left, 0.3, width, 0.4]
    rect3 = [left, 0.1, width, 0.2]

    axescolor = '#f6f6f6'  # the axes background color
    ax1 = fig.add_axes(rect1, facecolor=axescolor)  # left, bottom, width, height
    ax2 = fig.add_axes(rect2, facecolor=axescolor, sharex=ax1)
    ax2t = ax2.twinx()
    ax3 = fig.add_axes(rect3, facecolor=axescolor, sharex=ax1)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # max = len(WeatherData.objects.all())
    # if max > 5000: max = 5000
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # WeatherData.objects.filter(pressure_stn=0).delete()


    # #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # # num_int = int(num_str)
    # # if num_int == "1000":
    # #     pass
    # # num_int = WeatherData.objects.count()
    # # print("num_int=", num_int, "num=", num)
    #
    # # sel = WeatherData.objects.all()[num_int - max:num_int]   # last 1000
    sel = WeatherData.objects.all()
    # # sel = WeatherData.reverse()[:10000]   # last 1000
    #
    x = sel.values_list("grabbed_at")
    # print x[:]
    # x = [(21,), (20,), (15,)]

    y1 = sel.values_list("pressure_sea")
    y2 = sel.values_list("pressure_stn")
    # print y2[:]

    ax1.plot(x, y1, 'p-')
    ax1.plot(x, y2, 'g-')

    xfmt = DateFormatter('%d %b %H:%M') # xfmt = DateFormatter('%Y-%m-%d %H:%M')
    ax1.xaxis.set_major_formatter(xfmt)
    fig.autofmt_xdate()

    # plt.subplots_adjust(bottom=0.2)
    # plt.xticks( rotation=25 )
    # ax1=plt.gca()
    # plt.plot(dates,values)

    y3 = sel.values_list("temperature_air")
    y4 = sel.values_list("temperature_com")
    y5 = sel.values_list("temperature_dew")

    ax2 = ax1.twinx()
    ax2.plot(x, y3, 'b--')
    ax2.plot(x, y4, 'y--')
    ax2.plot(x, y5, 'r--')

    canvas = FigureCanvas(fig)

    return canvas


def weather_chart(request):

    canvas = weather_graph()

    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def clear_weather_data(request, numf="0", num_last="10", qw= True):

    # print ".'" * 20, "clear numbers=", num

    text = "<h2>HttpResponse:</h2>"
    text += "From"
    text += "<h3>num_first= " + numf + "</h3> to <h3>num_last= " + num_last + "</h3>"

    return HttpResponse(text)


class ClimateGraphView(TemplateView):

    template_name = 'records/climate_graph.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        canvas = weather_graph()

        # buffer = open('records/static/records/climate_graph.png', 'wb+')
        buffer = open('media/climate_graph.png', 'wb+')
        canvas.print_png(buffer)

        # response = HttpResponse(content_type='image/png')
        # canvas.print_png(response)

        context['mpl_image'] = buffer.read()
        context['latest_articles'] = 122
        return context





if __name__ == '__main__':

    weather_chart(None)




