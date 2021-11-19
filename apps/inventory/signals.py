from django.db.models.signals import post_save

from apps.inventory.models import ItemRevenue, ItemStock

def item_stock_edit(sender, instance, created, **kwargs):  
    pass    
