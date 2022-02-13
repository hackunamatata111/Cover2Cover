from django.contrib import admin

# Register your models here.

from .models import Profile, Take

admin.site.register(Take)
admin.site.register(Profile)
