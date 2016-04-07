#!/usr/bin/env python
# -*- coding: utf-8 -*-



# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response, get_object_or_404
# from django.template import RequestContext
#
# from polls.models import Choice, Poll
#
#
# def vote(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the poll voting form.
#         return render_to_response('polls/detail.html', {
#             'poll': p,
#             'error_message': "You didn't select a choice.",
#         }, context_instance=RequestContext(request))
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))

# add views here



from django.http import HttpResponse


import datetime
import ephem

import os
import sys


import scrapes.scrape_data2 as scr2
import scrapes.scrape_data3 as scr

import astro_routines.ephem1 as epph
import astro_routines.moon_day as md

import mysite.astro_routines.geo_place as geo
import mysite.astro_routines.geo_preload as geopr

import mysite.email_ASR as reminder



# def hello(request):
#
#     mars = ephem.Mars()
#     mars.compute('2015/3/17')
#     txtx = mars.ra
#
#     # return HttpResponse("Hello world...")
#     return HttpResponse(txtx)



# def current_datetime(request):
#     timenow = datetime.datetime.now()
#     html = "<html><body>" \
#            "Current time:%s. " \
#            "</body></html>" % timenow
#     return HttpResponse(html)



# from django.template import Template, Context
# person = {'name': ' Sally', 'age': '43'}
# t = Template('{{ person.name }} is {{ person.age }} years old.')
# cnt = Context({'person':person})
# t.render(cnt)
# # u'Sally is 43 years old.'



# from django.template.loader import get_template
# from django.template import Context
#
# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template('Current_date_time.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)




from django.shortcuts import render_to_response

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
    print "cur_date_utc=", cur_date_utc.strftime(format)

    tp, ctx2 = md.get_moon_day(cur_date_utc, coord)

    ctx += "\n" + ctx2
    print ctx

    return render_to_response('astro_data.html',
                              {'current_site':str(time_loc) + " " + cur_place,
                               'data_context':ctx})



def display_meta(request):
    values = request.META.items()

    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))

    return HttpResponse('<table>%s</table>' % '\n'.join(html))




def json_req(request):

    import json

    # response_data = {}
    # response_data['result'] = 'failed'
    # response_data['message'] = 'You messed up'
    # print response_data

    # response_data = md.get_phase_on_day(1)
    response_data = md.get_sun_on_month()

    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")



def main_index(request):

    reminder.email_reminder()   ###############################################

    s_out = "reminder.email_reminder()================"
    # for path in sys.path:
    #     print path
        # s_out += path + "\n"

    return render_to_response('Current_date_time.html', {'current_date': s_out})



# from django.http import JsonResponse
# return JsonResponse({'foo':'bar'})


# from django.http import JsonResponse
# ...
# return JsonResponse(array_to_js, safe=False)



# file charts.py








if __name__ == '__main__':

    # print locals()

    for path in sys.path:
        print path


    ctx = epph.sun_rise()
    print ctx


    # sys.path.pop(0)

    # sys.path.append("/home/flint/Projects/Py_projects/P_virtualenv/ENV_H/P_python-django-example-flint/mysite")


    # print "========================================"
    # for path in sys.path:
    #     print path


    # print sys.path
    # print scr


