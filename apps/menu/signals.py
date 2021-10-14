from django.db.models.signals import post_save

from apps.menu.models import Product 
from apps.menu.services.resize_image.pillow_image import resize_image

def  create_product(sender, instance, created, **kwargs):   
    # products/images/00000/00/00/.jpg
    if created:
        path = "media/" + str(instance.image)
        resize_image(path)
        
    else:
        if hasattr(instance, 'product'):
            path = "media/" + str(instance.image)
            resize_image(path)
            
        
post_save.connect(create_product, sender=Product)