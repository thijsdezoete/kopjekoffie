import os
import sys

wsgi_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.dirname(__file__) + '/koffie')
sys.path.append(project_dir)
project_settings = os.path.join(project_dir, 'koffie/settings')

#django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'koffie.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
