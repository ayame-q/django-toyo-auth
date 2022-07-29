__copyright__    = 'Copyright (C) 2021 ayame.space'
__version__      = '0.6.0'
__license__      = 'MIT'
__author__       = 'ayame.space'
__author_email__ = 'ayame.space@gmail.com'
__url__          = 'http://github.com/ayame-q/django-toyo-auth'

import django

if django.VERSION < (3, 2):
    default_app_config = "django_toyo_auth.apps.AccountsConfig"
