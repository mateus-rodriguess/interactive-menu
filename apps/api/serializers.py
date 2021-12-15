from rest_framework import serializers 
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock
from apps.menu.models import Category, Product


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

class IngredientSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', "description", 'pattern']

    def create(self, validated_data):
       
        return super().create(validated_data)

class ProductSerializers(serializers.ModelSerializer):
    ingredient =  IngredientSerializers(read_only=True)
    category = CategorySerializers(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description',
                  'price', 'available', 'ingredient']


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
    

