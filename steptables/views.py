from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from rnadimer.steptables.models import Forces
from rnadimer.steptables.models import Steps
from rnadimer.steptables.models import StepIds

import csv


def index(request):
    return render_to_response('index.htm')

def data(request):
    return render_to_response('data/data.htm')

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

def info(request):
    return render_to_response('info/info.htm',
    {'bpstep_list': StepIds.objects.order_by('ndb_id')},
    context_instance = RequestContext(request))

def news(request):
    return render_to_response('info/news.htm')


def credits(request):
    return render_to_response('info/credits.htm')

def references(request):
    return render_to_response('info/references.htm')

def stats(request):
    return render_to_response('stats/stats.htm')

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

def plot(request):
    import os
#    homies = 'Users/esguerra'
    homies = '/home/rnasteps'
    static = '/rnadimer/media/tmp'
    os.environ['HOME']=homies+static
    from numpy import *
    import csv    
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure

    rna     = open(homies+static+'/rnaonly.csv', 'r');
    dna     = open(homies+static+'/dnaonly.csv', 'r');
    protein = open(homies+static+'/proteins.csv','r');

    readrna = csv.reader(rna)        
    rnadata = []
    for row in readrna:
        rnadata.append(row)
    
    rna_arr = array(rnadata)
    
    readdna = csv.reader(dna)        
    dnadata = []
    for row in readdna:
        dnadata.append(row)
    
    dna_arr = array(dnadata)

    readprotein = csv.reader(protein)        
    proteindata = []
    for row in readprotein:
        proteindata.append(row)
    
    protein_arr = array(proteindata)
            
    
    fig=Figure()
    ax=fig.add_subplot(111)
    year = rna_arr[1:,0]
    yearly_rna = rna_arr[1:,1]
    yearly_dna = dna_arr[1:,1]
    yearly_protein = protein_arr[1:,1]    
#    yearlyfit = polyfit(year, yearly, 1)
    ax.set_yscale('log')
    ax.plot(year, yearly_rna,'o', color='red')
    leg1=ax.plot(year, yearly_rna,'b-', color='red')
    ax.plot(year, yearly_dna,'o', color='blue')
    leg2=ax.plot(year, yearly_dna,'b-', color='blue')
    ax.plot(year, yearly_protein,'o', color='green')
    leg3=ax.plot(year, yearly_protein,'b-', color='green')
    ax.grid(True,which="both")
    ax.set_xlim(1995, 2011)
    ax.set_rasterized(True)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Yearly Added Structures')    
    ax.set_title('Structures in PDB per Year')
    ax.legend((leg1,leg2,leg3),('RNA','DNA','Protein'), loc=4)
    
    canvas = FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


#def matplot(request):
#    import os
#    os.environ['HOME']='/Users/esguerra/rnadimer/media/tmp'
#    
#    inp = open("/Users/esguerra/rnadimer/media/tmp/sixbysix.dat");
#
#    #Arrange the data in an array
#    dist_arr = []
#    for line in inp.readlines():
#        dist_arr.append([])
#        for i in line.split():
#            dist_arr[-1].append(float(i))
#
#   inp.close()         
#   M = array(dist_arr)
#
#   plt.matshow(M)
#   plt.title('Distance Matrix of Ca to Ca distances.')
#   plt.xlabel('Residue Number Strand I')
#   plt.ylabel('Residue Number Strand II')
#   
#   canvas = FigureCanvas(plt.figure(1))
#   response=HttpResponse(content_type='image/png')
#   canvas.print_png(response)
#   return response
    
    
