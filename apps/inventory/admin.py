from django.contrib import admin
from .models import Item, Ingredient, ItemStock, ItemIngredient
from .forms import IngredientForm, ItemIngredientForm, ItemForm


class ItemRevenueInline(admin.TabularInline):
    model = ItemIngredient
    raw_id_fields = ['item']
    extra = 1
    form = ItemIngredientForm
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'status', 'created', 'updated']
    list_editable = ['status']
    form = ItemForm
    view_on_site = False


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'pattern', 'created', 'updated', 'pk']
    search_fields = ('name',)
    inlines = [ItemRevenueInline]
    view_on_site = False
    form = IngredientForm


@admin.register(ItemStock)
class ItemStockAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'potions', 'kilos', 'status']
    search_fields = ('item',)
    list_editable = ['quantity', 'potions', 'kilos', 'status']
    view_on_site = False


@admin.register(ItemIngredient)
class ItemIngredientAdmin(admin.ModelAdmin):
    list_display = ['item', 'ingredient', 'quantity', 'pk']
    search_fields = ('item',)
    view_on_site = False
