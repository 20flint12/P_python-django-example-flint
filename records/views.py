from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response

from django.http import HttpResponse




def search_form(request):
    return render_to_response('records_search_form.html')



def search(request):
    if 'q' in request.GET:
        message = 'You search %r' % request.GET['q']
    else:
        message = 'Blank form'
    return HttpResponse(message)




def search2(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q' ]
        books - Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Enter new req')

