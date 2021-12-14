from django.db.models.query import QuerySet
from rest_framework import generics
from apps.menu.models import Product
from apps.menu.api.serializers import ProductSerializers


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class SubjectDetailView(generics.RetrieveAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializers