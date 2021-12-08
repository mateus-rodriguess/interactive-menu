from django.db.models.signals import post_save

from apps.inventory.models import ItemStock, Item


def create_item_stock(sender, instance, created, **kwargs):  
    
    if created:
        ItemStock.objects.create(item=instance)    
    else:
        if hasattr(instance, 'ItemStock'):
            ItemStock.objects.create(item=instance)


post_save.connect(create_item_stock, sender=Item)