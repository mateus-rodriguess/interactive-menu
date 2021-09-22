from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from cpf_field.models import CPFField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile') 
    first_name = models.CharField(max_length=200, blank=True, unique=False, default="First name")
    last_name = models.CharField(max_length=200, blank=True,  unique=False, default="Last name")    
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
    
    