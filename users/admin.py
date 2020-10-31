from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

admin.site.site_header = 'LinkPeople Admin Panel'

    
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'country', 'city_or_district']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'country', 'city_or_district', 'password1', 'password2')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
