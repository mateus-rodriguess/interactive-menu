from django.db.models import query
from apps.api.serializers import (IngredientSerializers,
                                            ItemIngredientStockSerializers,
                                            ItemSerializers,
                                            ItemStockSerializers,
                                            ProductSerializers,
                                            CategorySerializers)
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.menu.models import Category, Product

class IngredientAdd(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers


class ItemtViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers


class ItemStockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemStock.objects.all()
    serializer_class = ItemStockSerializers


class ItemIngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemIngredient.objects.all()
    serializer_class = ItemIngredientStockSerializers


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers