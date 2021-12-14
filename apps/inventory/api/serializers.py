from rest_framework import serializers
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock


class IngredientSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', "description", 'pattern']


class ItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', "status"]


class ItemStockSerializers(serializers.ModelSerializer):
    item =  ItemSerializers(read_only=True)
    class Meta:
        model = ItemStock
        fields = ['item', 'quantity', "potions", "kilos", 'status']


class ItemIngredientStockSerializers(serializers.ModelSerializer):
    item =  ItemSerializers(read_only=True)
    ingredient =  IngredientSerializers(read_only=True)
    class Meta:
        model = ItemIngredient
        fields = ['id', 'item', "ingredient", "quantity", 'potions', 'kilos']