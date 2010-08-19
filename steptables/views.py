from django.shortcuts import render_to_response
from django.template import RequestContext
from rnadimer.steptables.models import Steps
import csv
from django.http import HttpResponse


#from rnadimer.steptables.models import Forces

def index(request):
    return render_to_response('index.htm')

def step_view(request):
    return render_to_response('steptables/steps.htm',
    {'step_list': Steps.objects.order_by('-count')},
    context_instance = RequestContext(request))

def csv_list(request):
    """ Renders a csv list  """
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=rnabps.csv'
    csv_steps = Steps.objects.all()

      # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Shift', 'Slide', 'Rise'])
    for (sh) in csv_steps:
        writer.writerow([sh.shift, sh.slide, sh.rise])
    return response

#    writer = csv.writer(response, dialect=csv.excel)
#    writer.writerow([Steps.objects('shift'), Steps.objects('slide')])
#    return response


#def search_form(request):
#    return render_to_response('search_form.html')

#def force_view(request):
#    return render_to_response('steptables/forces.html',
#    {'forces_list': Forces.objects.order_by('-stype')},
#    context_instance = RequestContext(request))
