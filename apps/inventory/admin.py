from django.contrib import admin
from .models import Item, Revenue, ItemStock, ItemRevenue
from .forms import RevenueForm, ItemRevenueForm, ItemForm


class ItemRevenueInline(admin.TabularInline):
    model = ItemRevenue
    extra = 1
    form = ItemRevenueForm
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'status', 'created', 'created']
    list_editable = ['status']
    form = ItemForm
    view_on_site = False



@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'pattern', 'created', 'created']
    search_fields = ('name',)
    inlines = [ItemRevenueInline]
    view_on_site = False
    form = RevenueForm



@admin.register(ItemStock)
class ItemStockAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'potions', 'kilos', 'status']
    search_fields = ('item',)
    list_editable = ['quantity', 'potions', 'kilos', 'status']
    view_on_site = False


@admin.register(ItemRevenue)
class ItemRevenueAdmin(admin.ModelAdmin):
    list_display = ['item', 'revenue', 'quantity']
    search_fields = ('item',)
    view_on_site = False
