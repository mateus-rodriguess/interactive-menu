from uuid import uuid4
from django.db import models
from django.urls import reverse
from apps.account.models import Profile


class Config(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=200, blank=True)
    slogan = models.ImageField(upload_to='slogan/images',blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


STATUS_ORDER_CHOICES = (
    ("FUC", "Funcionario"),
    ("GER", "Gerente"),
    ("GAR", "garçom"),
)


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    member = models.CharField(choices=STATUS_ORDER_CHOICES,blank=True, null=True, max_length=3)
    
    slug = models.SlugField(unique=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.profile)
    
    class Meta:
        ordering = ('profile',)
        verbose_name = "employe"
        verbose_name_plural = "employes"
    

    def get_absolute_url(self):
        return reverse("employee:employee-detail-view", kwargs={"slug": self.profile})