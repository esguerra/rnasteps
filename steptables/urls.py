from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('rnadimer.steptables.views',
#    (r'^', 'force_view'),                       
#    (r'^', 'step_view'),
#
    (r'^admin/(.*)', admin.site.root),
)






