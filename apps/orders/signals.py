from django.db.models.signals import post_save
from apps.orders.models import Order
from apps.inventory.services.order_stock import stock


def updadte_inventory(sender, instance, created, **kwargs):   
    if created:
        if instance.status == "Concluido" or instance.paid == True:
            stock(instance)
    else:
        if instance.status == "Concluido" or instance.paid == True:
            stock(instance)
        
post_save.connect(updadte_inventory, sender=Order)