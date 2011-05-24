import os

from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from rnadimer.steptables import views

admin.autodiscover()

#import os.path
#PROJECT_DIR = os.path.dirname(__file__)



urlpatterns = patterns('rnadimer.steptables.views',
    # Example:
    (r'^$', 'index'),
    (r'^download-form1/$', views.csv_list),
    (r'^download-form2/$', views.csv_list2),
    (r'^search/search-form/$', 'search_form'),
    (r'^search/', 'search'),                       
    (r'^info/', 'info'),           # Decoupling
    (r'^steps/', 'step_view'),     # Decoupling
    (r'^tests/', 'test_view'),     # Decoupling
    (r'^forces/', 'force_view'),   # Decoupling
    (r'^bpsteps/', 'bpstep_view'), # Decoupling                       
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root)
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.PROJECT_DIR,  'media')}),
    )
