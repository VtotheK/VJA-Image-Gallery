"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append(os.path.dirname(__file__))
from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ["DJANGO_SETTINGS_MODULE"] = 'project.settings'
application = get_wsgi_application()
