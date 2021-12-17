from apps.api.serializers import inventory_serializers, menu_serializers
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock
from apps.menu.models import Category, Product
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# class IngredientAdd(APIView):
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientSerializers


class ItemtViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemSerializers


class ItemStockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemStock.objects.all()
    serializer_class = inventory_serializers.ItemStockSerializers


class ItemIngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientSerializers


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = menu_serializers.ProductSerializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = menu_serializers.CategorySerializers
