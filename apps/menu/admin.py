from django.contrib import admin
from .models import Category, Product, Table


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    search_fields = ('name',)
    list_display_links = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
  

@admin.register(Table)
class tableAdmin(admin.ModelAdmin):
    list_display = ['number', 'max']
    