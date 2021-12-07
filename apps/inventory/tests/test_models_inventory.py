from re import I
import pytest
from apps.inventory.models import Item, ItemRevenue, Revenue


@pytest.fixture
def revenue(db):
    return Revenue.objects.create(name="pizza", description="pizza vegana")


@pytest.fixture()
def item(db, request):
    return Item.objects.create(name="alface")


def test_update_item(item):
    item.name = "repolho"
    item.save()
    item_from_db = Item.objects.get(name="repolho")
    assert item_from_db.name == "repolho"


def test_update_revenue(revenue):
    revenue.name = "humburguer"
    revenue.save()
    revenue_from_db = Revenue.objects.get(name="humburguer")
    assert revenue_from_db.name == "humburguer"


