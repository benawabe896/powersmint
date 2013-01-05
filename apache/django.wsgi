import os
import sys
 
path = '/var/www/mint'
if path not in sys.path:
    sys.path.insert(0, '/var/www/mint')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'mint.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
