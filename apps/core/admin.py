from django.contrib import admin
from .models import Config, Employee


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'created', 'updated', 'pk']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["profile", "member", "active", 'created', 'updated', 'pk']