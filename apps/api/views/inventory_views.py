from apps.api.serializers import inventory_serializers
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class IngredientView(generics.ListAPIView):
    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientSerializers


class IngredientCreate(generics.CreateAPIView):

    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientCreate


class IngredientUpdate(generics.UpdateAPIView):

    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientUpdateSerializers

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()


class IngredientDetailView(generics.RetrieveAPIView):

    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientSerializers


class ItemView(generics.ListAPIView):
   
    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemSerializers


class ItemDetailView(generics.RetrieveAPIView):

    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemSerializers


class IntemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemSerializers


class ItemStockView(generics.ListAPIView):
  
    queryset = ItemStock.objects.all()
    serializer_class = inventory_serializers.ItemStockSerializers


class ItemStockDetailView(generics.RetrieveAPIView):
    
    queryset = ItemStock.objects.all()
    serializer_class = inventory_serializers.ItemStockSerializers


class ItemIngredientView(generics.ListAPIView):
   
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientSerializers


class ItemIngredientDetailView(generics.RetrieveAPIView):

    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientSerializers


class ItemIngredientCreateView(generics.CreateAPIView):
    
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientCreateSerializers

class ItemIngredientUpdateView(generics.UpdateAPIView):
    
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientUpdateSerializers


class ItemIngredientDeleteView(generics.DestroyAPIView):
    
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientDeleteSerializers