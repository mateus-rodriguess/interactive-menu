from rest_framework import serializers
from apps.inventory.models import Ingredient
from apps.menu.models import Product, Category
from apps.inventory.api.serializers import IngredientSerializers, ItemSerializers


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializers(serializers.ModelSerializer):
    ingredient =  IngredientSerializers(read_only=True)
    category = CategorySerializers(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description',
                  'price', 'available', 'ingredient']





