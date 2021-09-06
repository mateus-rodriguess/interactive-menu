from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
# Create your models here.


class Table(models.Model):
    number = models.IntegerField(unique=True)
    # mais fields
    class Meta:
        verbose_name = ("table")
        verbose_name_plural = ("tables")

    def __str__(self):
        return self.number

    # não precisa disso, so quero salvar a mesa no banco de dados
    def get_absolute_url(self):
        return reverse("Table_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',
                                 on_delete=models.CASCADE)
    # vou ver depois como vai ficar isso
    #table = models.ForeignKey(Table,related_name='tables', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    # colocar por categoria depois
    image = models.ImageField(upload_to=f'products/images/%Y/%m/%d',blank=True)
   
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name
