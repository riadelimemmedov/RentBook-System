
#!Django Function
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

#!Models and Forms
from .models import (Account,Profile)
from .forms import (AccountForm)

# Register your models here.

#*AccountAdmin
@admin.register(Account)
class AccountAdmin(UserAdmin):
    form = AccountForm
    
    def thumbnail(self,object):
        if(object.photo):
            return format_html('<img src="{}" width="35" style="border-radius:50%;">'.format(object.photo.url))
        else:
            return format_html('<img src="https://i.stack.imgur.com/l60Hf.png" width="35" style="border-radius:50%;">')
    
        
    fieldsets = (
        (None,{"fields":('email','phone','password')}),
        (
            _('Personal info'),
            {
                "fields":(
                    "first_name",
                    "last_name",
                    'account_type',
                    "gender",
                    "photo",
                    "status",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields":("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    'account_type',
                    "gender",
                    "photo",
                    "status",
                    "phone",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = ("first_name","last_name","phone","is_staff","date_joined","last_login","thumbnail")
    list_filter = ("is_staff","is_superuser","is_admin","is_superadmin","is_active")
    list_display_links = ("thumbnail","first_name","last_name")
    search_fields = ("first_name", "last_name","email", "phone")
    readonly_fields = ("date_joined","last_login",'password')
    list_filter = ['first_name']
    filter_horizontal = ()
    

#*ProfileAdmin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['account','country','city','adress','slug']
    list_display_links = ['account']
