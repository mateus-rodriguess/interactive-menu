from django.db.models.signals import post_save
from django.conf import settings
from apps.menu.models import Product 
from apps.menu.services.resize_image.pillow_image import resize_image

def  create_product(sender, instance, created, **kwargs):   
  
    if created and instance.image:
        path = settings.MEDIA_URL[1:] + str(instance.image)
        resize_image(path)
        
    else:
        if hasattr(instance, 'product') and instance.image:
            path = settings.MEDIA_URL[1:] + str(instance.image)
            resize_image(path)
            

post_save.connect(create_product, sender=Product)




