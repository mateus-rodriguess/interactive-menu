from django.db import models
from django.db.models.fields import related
from apps.menu.models import Product
from apps.account.models import User


STATUS_ORDER_CHOICES = (
    ("CON", "Concluido"),
    ("NAC", "Não concluido"),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_ORDER_CHOICES,blank=True, null=True, max_length=3)
    note = models.CharField(blank=True, null=True, max_length=110, default="")
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


STATUS_ITEM_ORDER_CHOICES = (
    ("CON", "Concluido"),
    ("NAC", "Não concluido"),
    ("PRE", "Preparando"),
)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="itens", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)

    status = models.CharField(choices=STATUS_ITEM_ORDER_CHOICES, max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity