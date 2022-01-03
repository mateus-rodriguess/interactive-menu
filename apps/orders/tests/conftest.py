import pytest
from apps.account.models import User
from apps.inventory.models import Ingredient
from apps.menu.models import Category, Product
from apps.orders.models import Order, OrderItem


@pytest.fixture
def category(db):
    return Category.objects.create(name="pizza")


@pytest.fixture
def ingredient(db) :
    return Ingredient.objects.create(name="pizza", description="pizza vegana")


@pytest.fixture
def user(db):
    return User.objects.create(username="mateus", password="testes1234")


@pytest.fixture
def product(db, category, ingredient):
    return Product.objects.create(name="pizza", description="description product",
                                  price=22, category=category, ingredient=ingredient)


@pytest.fixture
def order(db, user):
    return Order.objects.create(user=user, status="NAC", paid=False, note="Nota")


@pytest.fixture
def order_item(db, product, order):
    return OrderItem.objects.create(order=order, product=product, status="PRE", price=20.00, quantity=1)
