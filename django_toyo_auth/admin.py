from django.contrib import admin
from .models import User

# Register your models here.
class UUIDFieldAdmin(admin.ModelAdmin):
    readonly_fields=('uuid',)


class UserAdmin(UUIDFieldAdmin):
    pass

admin.site.register(User, UserAdmin)