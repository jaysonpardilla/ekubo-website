"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""
import os
import sys

# Add the core directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
