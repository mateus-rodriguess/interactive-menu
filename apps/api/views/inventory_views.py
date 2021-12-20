from apps.api.serializers import inventory_serializers
from apps.inventory.models import Ingredient, Item, ItemIngredient, ItemStock
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class IngredientView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientSerializers


class IngredientCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientCreateSerializers


class IngredientUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientUpdateSerializers

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()


class IngredientDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientDeleteSerializers

    # def perform_destroy(self, instance):
    #     return super().perform_destroy(instance)


class IngredientDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ingredient.objects.all()
    serializer_class = inventory_serializers.IngredientSerializers


class ItemView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemSerializers


class ItemDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemSerializers


class ItemCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemCreateSerializers


class ItemUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemUpdateSerializers


class ItemDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = inventory_serializers.ItemDeleteSerializers


class ItemStockView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemStock.objects.all()
    serializer_class = inventory_serializers.ItemStockSerializers

    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)


class ItemStockDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemStock.objects.all()
    serializer_class = inventory_serializers.ItemStockSerializers


class ItemStockCreatelView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemStock.objects.all()
    serializer_class = inventory_serializers.ItemStockCreateSerializers


class ItemStockUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemStock.objects.all()
    serializer_class = inventory_serializers.ItemStockUpdateSerializers


class ItemStockDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemStock.objects.all()
    serializer_class = inventory_serializers.ItemStockDeleteSerializers


class ItemIngredientView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientSerializers


class ItemIngredientDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientSerializers


class ItemIngredientCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientCreateSerializers


class ItemIngredientUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientUpdateSerializers


class ItemIngredientDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ItemIngredient.objects.all()
    serializer_class = inventory_serializers.ItemIngredientDeleteSerializers
