"""User models amin."""

#django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#models
from c_zoo.users.models import User, Profile

class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display=('email','username', 'first_name','last_name','is_staff', 'is_client', 'is_admin')
    list_filter=('is_client','is_staff', 'created','modified')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile model admins."""

    #list_display=('user', 'reputation','rides_taken','rides_offered')
    list_display=('user','picture','biography')
    search_fields=('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter=('user__first_name',)

admin.site.register(User, CustomUserAdmin)