from django.db import models
from django.urls import reverse
# Create your models here.

STATUS_ITEM_CHOICES = (
    ("OK", "OK"),
    ("Ok", "OK"),
    ("OK", "OK"),
)

class Item(models.Model):
    name = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    
    quantity = models.PositiveIntegerField(default=1)
    potions = models.FloatField(blank=True, default=0, null=True)
    kilos = models.FloatField(blank=True, default=0, null=True)
    status = models.CharField(blank=True, choices=STATUS_ITEM_CHOICES, max_length=3, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
