from django.conf.urls.defaults import *
from django.contrib import admin
#from django.views.static import serve
from django.conf import settings
from rnadimer.steptables import views

admin.autodiscover()


urlpatterns = patterns('rnadimer.steptables.views',
    # Example:
    (r'^$', 'index'),
#    (r'^search-form/$', views.search_form),
    (r'^download-form/$', views.csv_list),
    (r'^steps/', include('rnadimer.steptables.urls')), # Decoupling
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root)
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/esguerra/rnadimer/media'}),
    )
