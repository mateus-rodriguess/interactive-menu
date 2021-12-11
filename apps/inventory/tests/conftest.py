import pytest
from apps.menu.models import Ingredient
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock


@pytest.fixture
def ingredient(db):
    return Ingredient.objects.create(name="pizza", description="pizza vegana")


@pytest.fixture()
def item(db):
    return Item.objects.create(name="alface")


@pytest.fixture
def item_ingredient(db, item, ingredient):
    return ItemIngredient.objects.create(item=item, ingredient=ingredient, quantity=53)


@pytest.fixture
def item_stock(db, item):
    return ItemStock.objects.create(item=item, quantity=30, potions=4, kilos=3)

