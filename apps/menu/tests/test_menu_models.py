import pytest
from mixer.backend.django import mixer
from apps.menu.models import Category, Product


@pytest.mark.django_db
class TestModel:

    def test_model_display_category(self):
        category = mixer.blend(Category, name="categoria")
        assert str(category) == "categoria"

    def test_model_display_product(self, category):
        product = mixer.blend(Product, category=category, price=30.00)
        assert str(product) == product.name
        assert product.category.pk == category.pk


def test_update_category(category):
    category.name = "pizza 2"
    category.save()
    category_from_db = Category.objects.get(name="pizza 2")
    assert category_from_db.name == "pizza 2"


def test_two_different_products_create(product_one, product_two):
    assert product_one.pk != product_two.pk
