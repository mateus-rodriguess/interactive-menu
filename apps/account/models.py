from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from cpf_field.models import CPFField
# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)    
    cpf = CPFField('cpf')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile') 

    slug = models.SlugField(max_length=200, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('first_name',)
        verbose_name = "profile"
        verbose_name_plural = "profiles"
    
    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('account:profile-detail-view', args=[self.slug])