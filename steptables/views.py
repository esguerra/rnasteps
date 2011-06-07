from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from rnadimer.steptables.models import Forces
from rnadimer.steptables.models import Steps
from rnadimer.steptables.models import StepIds

import csv


def index(request):
    return render_to_response('index.htm')

def force_view(request):
    return render_to_response('forcetables/forces.htm',
    {'force_list': Forces.objects.order_by('step_id')},
    context_instance = RequestContext(request))

def step_view(request):
    return render_to_response('steptables/steps.htm',
    {'step_list': Steps.objects.order_by('-count')},
    context_instance = RequestContext(request))

def test_view(request):
    return render_to_response('test_tables/test.htm',
    {'test_list': Steps.objects.filter(step_id='GG.CC')
     | Steps.objects.filter(step_id='CG.CG')},
    context_instance = RequestContext(request))

def cisww_view(request):
    return render_to_response('lwclass/cisww.htm',
    {'cisww_list': StepIds.objects.filter(gly_orie2='cis')},
    context_instance = RequestContext(request))

def transhs_view(request):
    return render_to_response('lwclass/transhs.htm',
    {'transhs_list': StepIds.objects.filter(edge3='H')
     & StepIds.objects.filter(edge4='S') },
    context_instance = RequestContext(request))

def transhw_view(request):
    return render_to_response('lwclass/transhw.htm',
    {'transhw_list': StepIds.objects.filter(edge3='H')
     & StepIds.objects.filter(edge4='W')},
    context_instance = RequestContext(request))


def info(request):
    return render_to_response('info/info.htm',
    {'bpstep_list': StepIds.objects.order_by('ndb_id')},
    context_instance = RequestContext(request))

def csv_list(request):
    """ Renders a csv list  """
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=rnabps.csv'
    csv_steps = Steps.objects.all()
      # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Step','Shift', 'Slide', 'Rise', 'Tilt', 'Roll', 'Twist'])
    for (sh) in csv_steps:
#        writer.writerow(["%.2f" % sh.step_id, sh.shift, sh.slide, sh.rise, sh.tilt, sh.roll, sh.twist])
#        writer.writerow([format(sh.step_id, '.2f'), sh.shift, sh.slide, sh.rise, sh.tilt, sh.roll, sh.twist])
        writer.writerow([sh.step_id, sh.shift, sh.slide, sh.rise, sh.tilt, sh.roll, sh.twist])
    return response


def csv_list2(request):
    """ Renders a csv list  """
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=rnaforces.csv'
    csv_forces = Forces.objects.all()
      # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Step','Shift', 'Slide', 'Rise', 'Tilt', 'Roll', 'Twist'])
    for (ch) in csv_forces:
        writer.writerow([ch.step_id, ch.shift, ch.slide, ch.rise, ch.tilt, ch.roll, ch.twist])
    return response



def search_form(request):
    return render_to_response('search/search_form.htm')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        return render_to_response('search/search_results.htm',
    {'stepid_list': StepIds.objects.filter(ndb_id__icontains=q)
     | StepIds.objects.filter(pdb_id__icontains=q), 'query': q}, 
    context_instance = RequestContext(request))

    else:
        return render_to_response('search/search_form.htm', {'error': True})


