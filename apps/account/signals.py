from django.db.models.signals import post_save
from django.contrib.auth.models import User

from apps.account.models import Profile


def  create_profile(sender, instance, created, **kwargs):    
    if created:
        Profile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)



post_save.connect(create_profile, sender=User)