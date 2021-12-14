from apps.inventory.api.serializers import (IngredientSerializers,
                                            ItemIngredientStockSerializers,
                                            ItemSerializers,
                                            ItemStockSerializers)
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class IngredientAdd(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
   
    def post(self, request, pk, format=None):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        
        return Response({'Alterado': True})


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
