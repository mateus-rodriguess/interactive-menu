import pytest
from apps.menu.models import Category, Product
from apps.menu.models import Ingredient


@pytest.fixture
def category(db) -> Category:
    return Category.objects.create(name="pizza")


@pytest.fixture
def ingredient(db):
    return Ingredient.objects.create(name="pizza", description="pizza vegana")


@pytest.fixture
def product_one(db, ingredient, category):
    return Product.objects.create(name="pizza", description="description product",
                                  price=22, category=category, ingredient=ingredient)


@pytest.fixture
def product_two(db, ingredient, category):
    return Product.objects.create(name="pizza 2", description="description product", price=22, category=category, ingredient=ingredient)
