"""
WSGI config for Mylinebot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from os.path import join,dirname,abspath
import sys
from django.core.wsgi import get_wsgi_application


# sys.path.append('/var/www/line-bot.dida-dream.com/Mylinebot')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mylinebot.settings')

application = get_wsgi_application()
