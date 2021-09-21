from django.contrib import admin
from django.contrib.admin.helpers import AdminForm
from .models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','CPF',]
    

