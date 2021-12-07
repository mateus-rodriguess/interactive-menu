import pytest
from mixer.backend.django import mixer
from apps.menu.models import Category, Table, Product
from apps.menu.models import Revenue


@pytest.mark.django_db
class TestModel:

    def test_create_category(self): ...
    # A uma fixture desse codigo pronto.....
    # category = Category.objects.create(name="Books")
    # assert category.name == "Books"
    # category.name = "pizza2"
    # category.save()
    # category_from_db = Category.objects.get(name="pizza2")
    # assert category_from_db.name == "pizza2"

    def test_model_display_category(self):
        category = mixer.blend(Category, name="categoria")
        assert str(category) == "categoria"

    def test_create_table(self):
        table = Table
        assert table.objects.count() == 0
        Table.objects.create(number=2, description="descrição", max=4)
        assert table.objects.count() == 1

    def test_model_display_table(self):
        table = mixer.blend(Table, number=5)
        assert str(table) == "5"


@pytest.fixture
def category(db) -> Category:
    return Category.objects.create(name="pizza")


def test_update_category(category):

    category.name = "pizza 2"
    category.save()
    category_from_db = Category.objects.get(name="pizza 2")
    assert category_from_db.name == "pizza 2"


@pytest.fixture
def product_one(db, revenue, category):
    return Product.objects.create(name="pizza", description="description product",
                                  price=22, category=category, revenue=revenue)


@pytest.fixture
def product_two(db, revenue, category):
    return Product.objects.create(name="pizza 2", description="description product" ,price=22, category=category, revenue=revenue)


def test_two_different_books_create(product_one, product_two):
    assert product_one.pk != product_two.pk
