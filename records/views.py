from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response

from django.http import HttpResponse

from records.models import Book



def search_form(request):

    # from records.models import Publisher
    p1 = Publisher(name='Apress2', address='2855 Telegraph Avenue',
        city='Berkeley', state_province='CA', country='U.S.A,',
        website='http://www.apress.com/')
    p1.save()
    p2 = Publisher(name="0'Reilly2", address='10 Fawcett St.',
        city='Cambridge', state_province='MA', country='U.S.A.',
        website='http://www.oreilly.com/')
    p2.save()

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
        books = Book.objects.filter(title__icontains=q)
        # books = Publisher.objects.all()
        print books
        return render_to_response('records_search_results.html',
            {'books': books, 'query': q})
    else:
        # return HttpResponse('Enter new req')
        return render_to_response('records_search_form.html', {'error': True})

