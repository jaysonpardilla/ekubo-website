"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""
import os
import sys

# Add the core directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# This line is crucial. It sets up Django's application registry.
django.setup()

# Now, you can safely import your routing.
from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
