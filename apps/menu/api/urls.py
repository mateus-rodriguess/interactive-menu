from django.urls import path
from . import views

app_name = "nemnu"

urlpatterns = [
    path("product/", views.ProductListView.as_view(), name="product_list"),
    path("product/<pk>/", views.SubjectDetailView.as_view(), name="product_detail"),
    
]
