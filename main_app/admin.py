from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Properties, ViewingRequest, UserProfile


@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'is_published')
    list_filter = ('is_published', 'available', 'list_date')
    actions = ['publish', 'toggle_availability']

    def publish(self, request, queryset):
        queryset.update(is_published=True)

    def toggle_availability(self, request, queryset):
        queryset.update(available=not queryset[0].available)


@admin.register(ViewingRequest)
class ViewingRequestAdmin(admin.ModelAdmin):
    list_filter = ('request_date', 'arranged_date', 'for_user')
    search_fields = (
        'for_user__email', 'for_user__first_name',
        'for_user__last_name')
    readonly_fields = ('property', 'message', 'request_date', 'for_user')


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
