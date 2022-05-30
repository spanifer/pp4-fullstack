from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Properties, ViewingRequest, UserProfile

admin.site.register(Properties)
admin.site.register(ViewingRequest)


# Solution from https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
# Add the UserProfile to the admin Users interface
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
