from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cartdetail', views.cart_detail, name='cart_detail'),
    path('add/<uuid:id>/', views.cart_add, name='cart_add'),
    path('remove/<uuid:id>/', views.cart_remove, name='cart_remove'),
]
