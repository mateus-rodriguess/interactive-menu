from django.db import models
from django.urls import reverse_lazy, reverse

from apps.menu.models import Product
from apps.account.models import User


MOVEMENT_CHOICES = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Inventory(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    movimento = models.CharField(
        max_length=1, choices=MOVEMENT_CHOICES, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "inventory"
        verbose_name_plural = "inventorys"

    def __str__(self):
        return f"{self.movimento}"

    def get_absolute_url(self):
        return reverse("inventory:inventory_detail", kwargs={"pk": self.pk})


class EstoqueItems(models.Model):
    Inventory = models.ForeignKey(Inventory,on_delete=models.CASCADE,
                                related_name='inventory')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f"{self.pk} - {self.estoque.pk} - {self.produto}"
