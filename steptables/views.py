from django.shortcuts import render_to_response
from django.template import RequestContext
from rnadimer.steptables.models import Steps
#from rnadimer.steptables.models import Forces

def index(request):
    return render_to_response('index.htm')

def step_view(request):
    return render_to_response('steptables/steps.htm',
    {'step_list': Steps.objects.order_by('-shift')},
    context_instance = RequestContext(request))

#def force_view(request):
#    return render_to_response('steptables/forces.html',
#    {'forces_list': Forces.objects.order_by('-stype')},
#    context_instance = RequestContext(request))
