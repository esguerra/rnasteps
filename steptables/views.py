from django.shortcuts import render_to_response
from django.template import RequestContext
from rnadimer.steptables.models import Steps

def index(request):
    return render_to_response('index.html')

#def shift_view(request):
#    step_list = Steps.objects.all().order_by('-shift')
#    return render_to_response('tablas/index.html', {'step_list': step_list})

def step_view(request):
    return render_to_response('steptables/index.html',
    {'step_list': Steps.objects.order_by('-shift')},
    context_instance = RequestContext(request))
    current_page = RequestContext(request)

#def slide_view(request):
#    m_list = Steps.objects.order_by('-slide')
#    return render_to_response('tablas/slide.html',
#    {'m_list': m_list},
#    context_instance = RequestContext(request))
#    current_page = RequestContext(request)



#def slide(request):
#    tablitas = Steps.objects.order_by('-slide')    
#    context = {
#        'tablitas':  tablitas,
#    }
#    return render_to_response(
#        'tablas/slide.html',
#    context,
#    context_instance = RequestContext(request),
#    )
    
    
# TO CONTINUE WATCH SCREENCAST 11



#    latest_steps_list = Steps.objects.all().order_by('-shift')[:5]
#    t = loader.get_template('tablas/index.html')
#    c = Context({
#        'latest_steps_list': latest_steps_list,
#    })
#    return HttpResponse(t.render(c))
