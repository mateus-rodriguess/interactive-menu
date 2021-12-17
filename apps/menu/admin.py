from django.contrib import admin
from .models import Category, Product
from .forms import ProductForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', "slug", 'price', 'available', 'created', 'updated', "pk"]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    search_fields = ('name',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}

   
