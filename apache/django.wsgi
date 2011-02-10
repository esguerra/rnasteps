import os, sys
sys.path.append('/home/rnasteps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rnadimer.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
