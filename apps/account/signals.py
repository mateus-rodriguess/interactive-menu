from django.db.models.signals import post_save

from apps.account.models import Profile, User


def  create_profile(sender, instance, created, **kwargs):    
    if created:
        Profile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)
        
        


post_save.connect(create_profile, sender=User)