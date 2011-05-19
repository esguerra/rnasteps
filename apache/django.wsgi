import os, sys

#path = '/home/rnasteps'
path = '/users/esguerra'

if path not in sys.path:
   sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'rnadimer.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
