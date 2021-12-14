from django.urls import path, include
from rest_framework import routers

from . import views
from . import viewsets 

app_name = "ingredient"


router = routers.DefaultRouter()
router.register('ingredient', viewsets.IngredientViewSet)
router.register('item', viewsets.ItemtViewSet)

router.register('item stock', viewsets.ItemStockViewSet)
router.register('item ingredient', viewsets.ItemIngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("ingredient/", views.IngredientView.as_view(), name="ingredient_list"),
    path("ingredient/<pk>/", views.IngredientDetailView.as_view(), name="ingredient_detail"),
   
    path("item/stock/", views.ItemStockView.as_view(), name="item_stock_list"),
    path("item/stock/<pk>/", views.ItemStockDetailView.as_view(), name="item_stock_detail"),

    
    path("item/ingredient/", views.ItemIngredientView.as_view(), name="item_ingredient_list"),
    path("item/ingredient/<pk>/", views.ItemIngredientDetailView.as_view(), name="item_ingredient_detail"),
    path("item/<pk>/ingredient/", viewsets.IngredientAdd.as_view(), name="item_ingredient_list_ok"),

    path("item/<pk>/", views.ItemDetailView.as_view(), name="item_detail"),
    path("item/", views.ItemView.as_view(), name="item_list"), 
]