from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('rnadimer.steptables.views',
    # Example:
    (r'^$', 'index'),
    (r'^steps/', include('rnadimer.steptables.urls')), # Decoupling
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
)
