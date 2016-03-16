#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime



from django.shortcuts import render


# Create your views here.

from django.shortcuts import render_to_response

from django.http import HttpResponse

from records.models import Book

from records.models import Publisher

from records.models import RecNews
from records.models import WeatherData

import records.scrapes.scrape_data3 as scr3
import records.scrapes.scrape_data2 as scr2





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
        q = request.GET['q' ]
        # books = Book.objects.filter(title__icontains=q)
        # books = Publisher.objects.all()
        books = Book.objects.all()
        # books = Publisher.objects.all()
        print books
        return render_to_response('records_search_results.html',
            {'books': books, 'query': q})
    else:
        # return HttpResponse('Enter new req')
        return render_to_response('records_search_form.html', {'error': True})




def news(request):

    dt = datetime.datetime.today()
    # str_date_stamp = dt.strftime('%YYYY-%MM-%DD')

    ctx = scr3.get_news()
    if ctx:
        n1 = RecNews(news_date=dt, news_contents=ctx)
        n1.save()

    print "+" * 100    #

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

    dt = datetime.datetime.today()
    ctx = scr2.parse_temperature(scr2.get_temperature())
    # ctx = [u'20:00', 23, 25, 10, 44, 768, 754]
    print "weather-!-" * 5, ctx

    if ctx:
        w = WeatherData(weather_datetime = dt,
                        check_time      = ctx[0],
                        temperature_air = ctx[1],
                        temperature_com = ctx[2],
                        temperature_dew = ctx[3],
                        temperature_hum = ctx[4],
                        pressure_sea    = ctx[5],
                        pressure_stn    = ctx[6])
        w.save()
        print "+" * 80




def weather_chart(request):

    import django

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    print ".'" * 20, "weather_chart", ".'" * 20

    #**************************************************************************
    #  x = np.arange(0, 10, 0.1)
    # y1 = 0.05 * x**2
    # y2 = -1 *y1
    #
    # fig, ax1 = plt.subplots()
    #
    # ax2 = ax1.twinx()
    # ax1.plot(x, y1, 'g-')
    # ax2.plot(x, y2, 'b-')
    #
    # ax1.set_xlabel('X data')
    # ax1.set_ylabel('Y1 data', color='g')
    # ax2.set_ylabel('Y2 data', color='b')
    #**************************************************************************

    fig=Figure(figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')
    ax1=fig.add_subplot(111)
    # ax1=fig.subplots_adjust(bottom=0.2)

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    max = len(WeatherData.objects.all())
    if max > 5000: max = 5000
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    WeatherData.objects.filter(pressure_stn=0).delete()

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    cnt = WeatherData.objects.count()
    sel = WeatherData.objects.all()[cnt-max:cnt]   # last 1000
    # sel = WeatherData.reverse()[:10000]   # last 1000

    x = sel.values_list("weather_datetime")
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




    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response







if __name__ == '__main__':

    weather_chart(None)




