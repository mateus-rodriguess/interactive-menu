from django.contrib import admin
from .models import EstoqueItems, Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass
    

@admin.register(EstoqueItems)
class EstoqueItemsAdmin(admin.ModelAdmin):
    pass
