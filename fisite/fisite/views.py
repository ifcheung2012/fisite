from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime
import time
from fisite.forms import ContactForm

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            return HttpResponseRedirect('/contact/')
    else:
        form=ContactForm()
    return render_to_response('contact_form.html',{'form':form})


def hello(request):
    #now=datetime.datetime.now()
    #meta=request.META['HTTP_USER_AGENT']
    #return HttpResponse("Hello world %s \n " % meta)
    values=request.META.items()
    values.sort()
    html=[]
    for k,v in values :
        html.append('<tr><td>%s</td></tr><tr><td>%s</td></tr>'% (k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.POST:
        message='you search for:%r'% request.POST['q']
    else:
        message='you submitted an empty form.'
    return HttpResponse(message)

def current_datetime(request):
    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    now=datetime.datetime.now()
    #t=get_template('current_datetime.html')
    #html=t.render(Context({'current_date':now}))
    #return HttpResponse(html)
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    #assert True
    html="<html><body>In %s hour(s),it will be %s.</body></html>" %(offset,dt)
    return HttpResponse(html)
