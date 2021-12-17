from apps.api.serializers.inventory_serializers import IngredientSerializers
from apps.menu.models import Category, Product
from rest_framework import serializers, status
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

    def create(self, validated_data):
        return super().create(validated_data)


class CategoryListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

    def update(self, instance, validated_data):

        return super().update(instance, validated_data)


class CategoryDeleteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializers(serializers.ModelSerializer, DestroyModelMixin):
    ingredient = IngredientSerializers(read_only=True)
    category = CategorySerializers(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description',
                  'price', 'available', 'ingredient']


class ProductDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
    ingredient = IngredientSerializers(read_only=True)
    category = CategorySerializers(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description',
                  'price', 'available', 'ingredient']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description',
                  'price', 'available', 'ingredient']

    def create(self, validated_data):

        return super().create(validated_data)


class ProductUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description',
                  'price', 'available', 'ingredient']

    def create(self, instance, validated_data):
        return super().update(instance, validated_data)


class ProductDestroySerializers(serializers.ModelSerializer, DestroyModelMixin):

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description',
                  'price', 'available', 'ingredient']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
