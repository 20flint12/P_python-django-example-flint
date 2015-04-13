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
# import ephem



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
    now = datetime.datetime.now()
    return render_to_response('Current_date_time.html', {'current_date': now})




# def current_datetime(request):
#     current_date = datetime.datetime.now()
#     return render_to_response('Current_date_time.html', locals())


import os
import sys


try:
    # Work for local
    # # sys.path.insert(0, '/home/flint/Projects/Py_projects/ENV_H/P_python-django-example-flint/scrapes/')
    # sys.path.insert(0, '/home/flint/Projects/Py_projects/ENV_H/P_python-django-example-flint/mysite/scrapes/')
    # # sys.path.insert(0, './scrapes/')

    # import scrape_data3 as scr
    import scrapes.scrape_data3 as scr

    # from /home/flint/Projects/Py_projects/ENV_H/' \
    #      'P_python-django-example-flint/scrapes/' import scrape_data3 as scr

    scriptPath = os.path.realpath(os.path.dirname(__name__))
    print "scriptPath >>>>>>>>>>", scriptPath




    # first change the cwd to the script path
    # scriptPath = os.path.realpath(os.path.dirname(__name__))
    # print "scriptPath >>>>>>>>>>", scriptPath
    # os.chdir(scriptPath)
    # #append the relative location you want to import from
    # sys.path.append("..P_scrape_web")
    # import scrape_data3 as scr
    #

    # import scrapes.scrape_data3 as scr


    # from mysite.P_scrape_web2 \
    # import scrape_data3


    # from ..P_scrape_web import scrape_data3
    print "ImportOk"
except ImportError:
    print "ImportError ###############"
    # import connection_setting_MAG as conn





def scrape_data_req(request):
    now = datetime.datetime.now()
    # cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    news = scr.get_news()
    return render_to_response('scrape_data.html',
                              {'current_site':now,
                               'data_context':news})






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


