#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime



from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response

from django.http import HttpResponse

from records.models import Book



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



from records.models import Publisher

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




from records.models import RecNews
from records.models import WeatherData

import mysite.scrapes.scrape_data3 as scr3
import mysite.scrapes.scrape_data2 as scr2

import multiprocessing as mp



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
    delta_time = datetime.timedelta(days=0,
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
                print "+" * 100

            time.sleep(60)

        print "my_proc_exec is finished"

    except KeyboardInterrupt:

        print '^C received, break'




def weather_chart(request):

    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    print "!.'" * 100

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]


    x = WeatherData.objects.all().values_list("weather_datetime")
    # x = [(21,), (20,), (15,)]
    print x[:]
    y = WeatherData.objects.all().values_list("temperature_air")
    # y = [(23,), (24,), (35,)]
    print y[:]


    # now=datetime.datetime.now()
    # delta=datetime.timedelta(days=4)
    # for i in range(30):
    #     x.append(now)
    #     now+=delta
    #     y.append(random.randint(0, 1000))
    #

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




