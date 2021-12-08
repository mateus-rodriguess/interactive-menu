from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from cpf_field.models import CPFField


class User(AbstractUser):
    CPF = CPFField('cpf')
    slug = models.SlugField(max_length=150, unique=True)
    
    def get_absolute_url(self):
        return reverse('account:profile-detail-view', args=[self.username])
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile') 
    first_name = models.CharField(max_length=100, blank=True, unique=False, default="Nome")
    last_name = models.CharField(max_length=100, blank=True,  unique=False, default="Sobrenome")    
    
    slug = models.SlugField(max_length=150,unique=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = "profile"
        verbose_name_plural = "profiles"
    
    def __str__(self):
        return f"{self.first_name} - {self.user}" 

    def get_absolute_url(self):
        return reverse("account:profile-detail-view", args=[self.user])
    