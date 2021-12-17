from rest_framework import serializers, status
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response

class IngredientSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', "description", 'pattern']


class IngredientCreate(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', "description", 'pattern']

    def create(self, validated_data):
       
        return super().create(validated_data)


class IngredientUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', "description", 'pattern']

    def update(self, instance, validated_data):
        
        return super().update(instance, validated_data)


class ItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name', "status"]


class ItemStockSerializers(serializers.ModelSerializer):
    item =  ItemSerializers(read_only=True)
    
    class Meta:
        model = ItemStock
        fields = ['item', 'quantity', "potions", "kilos", 'status']


class ItemIngredientSerializers(serializers.ModelSerializer):
    # item =  ItemSerializers(read_only=True)
    #ingredient =  IngredientSerializers(read_only=True)
    
    class Meta:
        model = ItemIngredient
        fields = ['id', 'item', "ingredient", "quantity", 'potions', 'kilos']
    

class ItemIngredientCreateSerializers(serializers.ModelSerializer):
    # item =  ItemSerializers(read_only=True)
    #ingredient =  IngredientSerializers(read_only=True)
    
    class Meta:
        model = ItemIngredient
        fields = ['id', 'item', "ingredient", "quantity", 'potions', 'kilos']
    
    def create(self, validated_data):

        return super().create(validated_data)
    
class ItemIngredientUpdateSerializers(serializers.ModelSerializer):
    # item =  ItemSerializers(read_only=True)
    #ingredient =  IngredientSerializers(read_only=True)
    
    class Meta:
        model = ItemIngredient
        fields = ['id', 'item', "ingredient", "quantity", 'potions', 'kilos']
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ItemIngredientDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
    # item =  ItemSerializers(read_only=True)
    #ingredient =  IngredientSerializers(read_only=True)
    
    class Meta:
        model = ItemIngredient
        fields = ['id', 'item', "ingredient", "quantity", 'potions', 'kilos']
  
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)