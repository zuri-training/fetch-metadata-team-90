"""
ASGI config for fetchMetadata project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fetchMetadata.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

from configurations.asgi import get_asgi_application


application = get_asgi_application()
