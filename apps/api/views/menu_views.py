from apps.api.serializers import menu_serializers
from apps.menu.models import Category, Product
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ProductListView(generics.ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = menu_serializers.ProductSerializers


class ProductDetailView(generics.RetrieveAPIView):
    queryset =  Product.objects.all()
    serializer_class = menu_serializers.ProductSerializers


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    queryset =  Product.objects.all()
    serializer_class =  menu_serializers.ProductCreateSerializers


class ProductDestroyView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset =  Product.objects.all()
    serializer_class = menu_serializers.ProductDeleteSerializers

    # pode fazer desse jeito tambem
    # def perform_destroy(self, instance):
    #     return super().perform_destroy(instance)


class ProductUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset =  Product.objects.all()
    serializer_class = menu_serializers.ProductUpdateSerializers
    

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = menu_serializers.CategoryListSerializers


class CategoryCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = menu_serializers.CategoryCreateSerializers


class CategoryDetailView(generics.RetrieveAPIView):
  
    queryset = Category.objects.all()
    serializer_class = menu_serializers.CategorySerializers


class CategoryUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = menu_serializers.CategoryUpdateSerializers


class CategoryDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = menu_serializers.CategoryDeleteSerializers

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    