import pytest
from mixer.backend.django import mixer
from apps.menu.models import Category


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


def test_update_category(category):
    category.name = "pizza 2"
    category.save()
    category_from_db = Category.objects.get(name="pizza 2")
    assert category_from_db.name == "pizza 2"


def test_two_different_books_create(product_one, product_two):
    assert product_one.pk != product_two.pk
