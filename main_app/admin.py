from django.contrib import admin
from .models import Properties, ViewingRequest, UserProfile

admin.site.register(UserProfile)
admin.site.register(Properties)
admin.site.register(ViewingRequest)
