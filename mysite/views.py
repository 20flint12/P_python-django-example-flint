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
#

# add views here





from django.http import HttpResponse

import datetime
import ephem



def hello(request):

    mars = ephem.Mars()
    mars.compute('2015/3/17')
    txtx = mars.ra

    # return HttpResponse("Hello world...")
    return HttpResponse(txtx)



def current_datetime(request):
    timenow = datetime.datetime.now()
    html = "<html><body>" \
           "Current time:%s. " \
           "</body></html>" % timenow
    return HttpResponse(html)