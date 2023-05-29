from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Company, User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'role', 'company']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'role', 'company')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'role', 'company')}),
    )



admin.site.register(Company)
admin.site.register(User, UserAdmin)
