from django.db.models.signals import post_save, pre_save

from apps.menu.models import Product 


def  create_product(sender, instance, created, **kwargs):   
    print("pasosu aqui") 
    if created:
        print(instance)
        
           

post_save.connect(create_product, sender=Product)