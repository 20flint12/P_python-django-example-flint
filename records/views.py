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

import mysite.scrapes.scrape_data3 as scr3
import mysite.scrapes.scrape_data2 as scr2

import multiprocessing as mp


import mysite.email_ASR as reminder




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

    # my_proc_exec = mp.Process(target=my_proc_news,
    #                           args=(3,) )
    # my_proc_exec.start()


    # dt = datetime.datetime.today()
    # str_date_stamp = dt.strftime('%YYYY-%MM-%DD')
    # # print dt, str_date_stamp
    #
    # ctx = scr2.get_temperature()
    # # ctx = scr3.get_news()
    #
    # # ustring = unicode(read_string, encoding=...)
    # n1 = RecNews(news_date=dt, news_contents=ctx)
    # n1.save()

    books = RecNews.objects.all()
    return render_to_response('news_search_results.html',
        {'books': books})



# def my_proc_news(repeat_counter):
#
#     # repeat = 1
#
#     begin_time = datetime.datetime.now()
#     print "\nBegin time:", str(begin_time)[:-7]
#     cur_time = begin_time
#     delta_time = datetime.timedelta(hours=0, minutes=20, seconds=30)
#     checkout_time = begin_time + delta_time
#
#     try:
#         while True:
#
#             # if repeat > repeat_counter:
#             #     break
#             #
#             # repeat += 1
#
#             if datetime.datetime.now() > checkout_time:
#
#                 break
#                 # Save full_str to file
#                 checkout_time = datetime.datetime.now() + delta_time
#
#
#             dt = datetime.datetime.today()
#             # ctx = scr2.get_temperature()
#             ctx = scr3.get_news()
#
#             if ctx:
#                 n1 = RecNews(news_date=dt, news_contents=ctx)
#                 n1.save()
#
#             print "+" * 100
#             # break
#             time.sleep(60)
#
#     except KeyboardInterrupt:
#
#         print '^C received, break'





my_proc_exec = mp.Process()

def weather(request):

    global my_proc_exec

    reminder.email_reminder()   ###############################################

    if my_proc_exec.is_alive():
        print "my_proc_exec is alive"
    else:
        my_proc_exec = mp.Process(target=my_proc_weather,
                                  args=(3,) )
        my_proc_exec.start()
        print "my_proc_exec is started"

    print "my_proc_exec=", my_proc_exec


    # dt = datetime.datetime.today()
    # str_date_stamp = dt.strftime('%YYYY-%MM-%DD')
    # print dt, str_date_stamp

    # ctx = scr2.get_temperature()
    # ctx = "efwoefлдо   ывдпалырвплы"
    # # ctx = scr3.get_news()
    #
    # # ustring = unicode(read_string, encoding=...)
    # n1 = RecNews(news_date=dt, news_contents=ctx)
    # n1.save()

    wdata = WeatherData.objects.all()
    # print wdata
    return render_to_response('news_search_results.html',
        {'books': wdata})




def my_proc_weather(repeat_counter):

    # repeat = 1

    begin_time = datetime.datetime.now()
    print "\nBegin time:", str(begin_time)[:-7]
    cur_time = begin_time
    delta_time = datetime.timedelta(days=30,
                                    hours=10,
                                    minutes=3,
                                    seconds=10)
    checkout_time = begin_time + delta_time

    try:
        while True:

            if datetime.datetime.now() > checkout_time:
                break
                checkout_time = datetime.datetime.now() + delta_time


            dt = datetime.datetime.today()
            ctx = scr2.parse_temperature(scr2.get_temperature())
            # ctx = [u'20:00', 23, 25, 10, 44, 768, 754]
            print "weather-" * 5, ctx

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

            time.sleep(60)

        print "my_proc_exec is finished"

    except KeyboardInterrupt:

        print '^C received, break'




def weather_chart(request):

    import django

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    print ".'" * 20, "weather_chart", ".'" * 20

    # fig=Figure()
    fig=Figure(figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')
    # fig(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

    ax=fig.add_subplot(111)
    x=[]
    y=[]


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

    # y = sel.values_list("temperature_air")
    y = sel.values_list("pressure_stn")
    # print y[:]


    ax.plot(x, y, '-')
    # ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    xfmt = DateFormatter('%Y-%m-%d %H:%M')
    ax.xaxis.set_major_formatter(xfmt)
    fig.autofmt_xdate()


    # plt.subplots_adjust(bottom=0.2)
    # plt.xticks( rotation=25 )
    # ax=plt.gca()
    # xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    # ax.xaxis.set_major_formatter(xfmt)
    # plt.plot(dates,values)


    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response







if __name__ == '__main__':

    weather_chart(None)




