from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username','admin','staff','active')
    list_filter = ('admin','staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','profile','background','About')}),
        ('Permissions', {'fields': ('admin','staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('profile','email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)