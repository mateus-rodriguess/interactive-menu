from django.db.models.signals import post_save
from django.conf import settings
from apps import orders
from apps.inventory.models import ItemStock
from apps.orders.models import Order, OrderItem
from apps.menu.models import Product
from apps.inventory.models import Revenue



def updadte_inventory(sender, instance, created, **kwargs):   
    if created:
        pass        
    else:

        order_item = OrderItem.objects.filter(order=instance)
        print(order_item)
       
        for item_list in  order_item:
            print(item_list.product)
            
            product = Product.objects.get(pk=item_list.product.pk)
            revenue =  Revenue.objects.get(pk=product)
            item_stock = ItemStock.objects.get()
            print("ok")



           

post_save.connect(updadte_inventory, sender=Order)