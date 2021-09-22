from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from .utils import get_random_code
from django.template.defaultfilters import slugify
from cpf_field.models import CPFField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile') 
    first_name = models.CharField(max_length=100, blank=True, unique=False, default="First name")
    last_name = models.CharField(max_length=100, blank=True,  unique=False, default="Last name")    
    CPF = CPFField('cpf')
    
    slug = models.SlugField(unique=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = "profile"
        verbose_name_plural = "profiles"
    
    def __str__(self):
        return f"{self.first_name} - {self.CPF[0:4]}" 

    def get_absolute_url(self):
        return reverse("account:profile-detail-view", kwargs={"slug": self.user})
    
    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name

    def save(self, *args, **kwargs):
        ex = False
        to_slug = self.slug
        if self.first_name != self.__initial_first_name or self.last_name != self.__initial_last_name or self.slug=="":
            if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
                ex = Profile.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Profile.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)