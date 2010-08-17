import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'rnadimer.settings'

sys.path.append('/home/esguerra/rnadimer')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
