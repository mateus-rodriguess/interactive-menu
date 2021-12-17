from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from apps.inventory.models import Ingredient


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('menu:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200)

    image = models.ImageField(
        upload_to=f'products/images/%Y/%m/%d/', blank=True)

    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
   
    objects = models.Manager()
    available_mamager = AvailableManager()

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('menu:product_detail', args=[self.id, self.slug])

   