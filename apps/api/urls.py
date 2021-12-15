from django.urls import include, path
from rest_framework import routers

from .views.inventory import (IngredientCreate, IngredientDetailView,
                              IngredientView, ItemDetailView,
                              ItemIngredientDetailView, ItemIngredientView,
                              ItemStockDetailView, ItemStockView, ItemView)
from .viewsets.viewsets import (CategoryViewSet, IngredientViewSet,
                                ItemIngredientViewSet, ItemStockViewSet,
                                ItemtViewSet, ProductViewSet)

app_name = "api"

router = routers.DefaultRouter()
# app invetory
router.register('Ingredient', IngredientViewSet)
router.register('Item', ItemtViewSet)
router.register('Item stock', ItemStockViewSet)
router.register('Item ingredient', ItemIngredientViewSet)
# app menu
router.register('Product', ProductViewSet)
router.register('Category', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path("add/ingredient/", IngredientCreate.as_view(), name="ingredient_app"),
    path("ingredient/", IngredientView.as_view(), name="ingredient_list"),
    path("ingredient/<pk>/", IngredientDetailView.as_view(),
         name="ingredient_detail"),

    path("item/stock/", ItemStockView.as_view(), name="item_stock_list"),
    path("item/stock/<pk>/", ItemStockDetailView.as_view(),
         name="item_stock_detail"),


    path("item/ingredient/", ItemIngredientView.as_view(),
         name="item_ingredient_list"),
    path("item/ingredient/<pk>/", ItemIngredientDetailView.as_view(),
         name="item_ingredient_detail"),

    path("item/<pk>/", ItemDetailView.as_view(), name="item_detail"),
    path("item/", ItemView.as_view(), name="item_list"),
]
