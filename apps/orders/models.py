from django.db import models
from django.contrib.auth.models import User

from apps.menu.models import Product, Table
from apps.account.models import Profile



STATUS_ORDER_CHOICES = (
    ("Concluido", "Concluido"),
    ("Não concluido", "Não concluido"),
)


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    table = models.ManyToManyField(Table,blank=True, null=True, default=1)

    paid = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_ORDER_CHOICES, max_length=50)
    note = models.CharField(null=True, blank=True , max_length=110, default=" ")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


STATUS_ITEM_ORDER_CHOICES = (
    ("Concluido", "Concluido"),
    ("Não concluido", "Não concluido"),
    ("Preparando", "Preparando"),
)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="itens", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)

    status = models.CharField(choices=STATUS_ITEM_ORDER_CHOICES, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
   
 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity