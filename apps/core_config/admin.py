from django.contrib import admin
from .models import Config
# Register your models here


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']

