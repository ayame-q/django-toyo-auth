from django.contrib import admin
from . import models
from django_toyo_auth.admin import UUIDToyoUserAdmin

admin.site.register(models.User, UUIDToyoUserAdmin)
