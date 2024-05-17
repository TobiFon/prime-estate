from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .fomrs import CustomUserChanageForm, CustomUserCreationForm
from .models import User



class CustomUserAdmin(UserAdmin):
    
    model = User
    form = CustomUserChanageForm
    add_form = CustomUserCreationForm
    list_display = ['id', 'username', 'email', 'first_name', 'last_name']


admin.site.register(User, CustomUserAdmin)