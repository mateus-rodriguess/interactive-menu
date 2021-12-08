import pytest
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


def test_update_item(item):
    item.name = "repolho"
    item.save()
    item_from_db = Item.objects.get(name="repolho")
    assert item_from_db.name == "repolho"


def test_update_revenue(ingredient):
    ingredient.name = "humburguer"
    ingredient.save()
    revenue_from_db = Ingredient.objects.get(name="humburguer")
    assert revenue_from_db.name == "humburguer"


def test_update_item_ingredient(item_ingredient):
    item_ingredient.quantity = 60
    item_ingredient.save()
    assert item_ingredient.quantity == 60


def test_update_item_stock(item_stock):
    item_stock.quantity = 20
    item_stock.potions = 5
    item_stock.kilos = 10
    item_stock.save()
    assert item_stock.quantity == 20 and item_stock.potions == 5 and item_stock.kilos == 10
