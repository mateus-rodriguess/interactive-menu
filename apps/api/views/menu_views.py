from apps.api.serializers.menu_serializers import (CategoryCreateSerializers,
                                       CategoryListSerializers,
                                       CategorySerializers,
                                       CategoryUpdateSerializers,
                                       ProductCreateSerializers,
                                       ProductSerializers,
                                       ProductUpdateSerializers,
                                       ProductDeleteSerializers,
                                       CategoryDeleteSerializers)
from apps.menu.models import Category, Product
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    #permission_classes = [IsAdminUser]


class ProductDetailView(generics.RetrieveAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializers


class ProductCreateView(generics.CreateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductCreateSerializers


class ProductDestroyView(generics.DestroyAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductDeleteSerializers

    # pode fazer desse jeito tambem
    # def perform_destroy(self, instance):
    #     return super().perform_destroy(instance)


class ProductUpdateView(generics.UpdateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductUpdateSerializers
    

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class CategoryCraateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializers


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializers


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializers

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    