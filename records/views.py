
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

import mysite.scrapes.scrape_data3 as scr
import mysite.scrapes.scrape_data2 as scr2

import multiprocessing as mp



def news(request):

    # if my_proc_exec.is_alive():
    #
    #     pass
    #
    # else:
    my_proc_exec = mp.Process(target=my_proc,
                              args=(3,) )
    my_proc_exec.start()


    dt = datetime.datetime.today()
    str_date_stamp = dt.strftime('%YYYY-%MM-%DD')
    # print dt, str_date_stamp

    ctx = scr2.get_temperature()
    # ctx = scr.get_news()

    n1 = RecNews(news_date=dt, news_contents=ctx)
    n1.save()

    books = RecNews.objects.all()
    print books
    return render_to_response('news_search_results.html',
        {'books': books})





def my_proc(repeat_counter):

    # repeat = 1

    begin_time = datetime.datetime.now()
    print "\nBegin time:", str(begin_time)[:-7]
    cur_time = begin_time
    delta_time = datetime.timedelta(hours=0, minutes=20, seconds=30)
    checkout_time = begin_time + delta_time

    try:
        while True:

            # if repeat > repeat_counter:
            #     break
            #
            # repeat += 1

            if datetime.datetime.now() > checkout_time:

                break
                # Save full_str to file
                checkout_time = datetime.datetime.now() + delta_time


            dt = datetime.datetime.today()
            # ctx = scr2.get_temperature()
            ctx = scr.get_news()

            n1 = RecNews(news_date=dt, news_contents=ctx)
            n1.save()

            print "+" * 100

            # break

            time.sleep(60)

    except KeyboardInterrupt:

        print '^C received, break'

