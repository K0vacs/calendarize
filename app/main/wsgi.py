"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()
main = os.path.expanduser('~/')
load_dotenv(os.path.join(main, '.env'))
