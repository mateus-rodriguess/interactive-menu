from django.db.models.signals import post_save

from apps.account.models import Profile, User


def  create_profile(sender, instance, created, **kwargs):    
    if created:
        Profile.objects.create(user=instance, slug=instance.slug)
    else:
        if hasattr(instance, 'profile'):
            Profile.objects.create(user=instance, slug=instance.slug)
        
        


post_save.connect(create_profile, sender=User)