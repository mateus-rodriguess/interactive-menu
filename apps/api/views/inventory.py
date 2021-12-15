from apps.api.serializers import (IngredientSerializers,
                                            ItemIngredientStockSerializers,
                                            ItemSerializers,
                                            ItemStockSerializers)
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class IngredientView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers


class IngredientCreate(generics.CreateAPIView):
   
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers    
   

class IngredientDetailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers


class ItemView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Item.objects.all()
    serializer_class = ItemSerializers


class ItemDetailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Item.objects.all()
    serializer_class = ItemSerializers

class IntemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers 

class ItemStockView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ItemStock.objects.all()
    serializer_class = ItemStockSerializers


class ItemStockDetailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ItemStock.objects.all()
    serializer_class = ItemStockSerializers


class ItemIngredientView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = ItemIngredient.objects.all()
    serializer_class = ItemIngredientStockSerializers


class ItemIngredientDetailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    queryset = ItemIngredient.objects.all()
    serializer_class = ItemIngredientStockSerializers
