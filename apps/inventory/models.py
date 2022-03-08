from uuid import uuid4
from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=140, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    pattern = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredient"

    def __str__(self):
        return f"{self.name} - " + "Padrao" if self.pattern == True else "Modificada"

    def get_absolute_url(self):
        return reverse("Ingredient_detail", kwargs={"pk": self.pk})


STATUS_ITEM_CHOICES = (
    ("OK", "OK"),
    ("SE", "Sem estoque"),

)


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=140, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    status = models.CharField(blank=True, choices=STATUS_ITEM_CHOICES,
                              max_length=3, null=True)

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


STATUS_ITEM_STOCK_CHOICES = (
    ("OK", "OK"),
    ("SE", "Sem estoque"),
)


class ItemStock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=False)
    potions = models.FloatField(blank=False, default=0, null=False)
    kilos = models.FloatField(blank=False, default=0, null=False)
    status = models.CharField(blank=True, choices=STATUS_ITEM_STOCK_CHOICES,
                              max_length=3, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('pk',)
        verbose_name = "item stock"
        verbose_name_plural = "item stocks"

    def __str__(self):
        return f"{self.item.name}"

    def get_absolute_url(self):
        return reverse("item_stock_detail", kwargs={"pk": self.pk})


class ItemIngredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, null=False)
    potions = models.FloatField(blank=False, default=0, null=False)
    kilos = models.FloatField(blank=False, default=0, null=False)

    class Meta:
        ordering = ('pk',)
        verbose_name = "Item ingredient"
        verbose_name_plural = "Item ingredient"

    def __str__(self):
        return f"{self.item.name}"
