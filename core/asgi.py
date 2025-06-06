"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from settings.base import DEBUG

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.dev' if DEBUG else 'settings.prod')

application = get_asgi_application()
