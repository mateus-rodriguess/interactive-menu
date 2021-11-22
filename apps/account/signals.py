from django.db.models.signals import post_save

from apps.account.models import Profile, User


def  create_profile(sender, instance, created, **kwargs):    
    if created:
        Profile.objects.create(user=instance, slug=instance.username)
    else:
        if hasattr(instance, 'profile'):
            Profile.objects.create(user=instance, slug=instance.username)
        else:
            # esse codigo se torna obsoleto 
            try:
                profile = Profile.objects.get(user=instance)   
                profile.slug = instance.username
                profile.save()
            except:
                print("erro no user name slug")
           

post_save.connect(create_profile, sender=User)