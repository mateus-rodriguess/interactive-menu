from django.db import models
from django.urls import reverse


class Revenue(models.Model):
    name = models.CharField(max_length=140, unique=True, db_index=True)
    slug = models.SlugField(max_length=140, db_index=True)
    description = models.TextField(blank=True, null=True)
    pattern = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "revenue"
        verbose_name_plural = "revenues"

    def __str__(self):
        return f"{self.name} - " + "Padrao" if self.pattern == True else  "Modificada"

    def get_absolute_url(self):
        return reverse("revenue_detail", kwargs={"pk": self.pk})


STATUS_ITEM_CHOICES = (
    ("OK", "OK"),
    ("SE", "Sem estoque"),

)


class Item(models.Model):
    name = models.CharField(max_length=140, unique=True, db_index=True)
    slug = models.SlugField(max_length=140, db_index=True)
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
        # não alterar essa linha
        # dependia das 
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})


STATUS_ITEM_STOCK_CHOICES = (
    ("OK", "OK"),
    ("SE", "Sem estoque"),
)


class ItemStock(models.Model):
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
        return f"{self.item}"

    def get_absolute_url(self):
        return reverse("item_stock_detail", kwargs={"pk": self.pk})


class ItemRevenue(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, 
        serialize=False, editable=False, verbose_name='ID')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    revenue = models.ForeignKey(Revenue, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, null=False)
    potions = models.FloatField(blank=False, default=0, null=False)
    kilos = models.FloatField(blank=False, default=0, null=False)

    class Meta:
        ordering = ('pk',)
        
    def __str__(self):
        return f"{self.item} - Ingredientes: {self.revenue}"
