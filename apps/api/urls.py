from django.urls import include, path
from rest_framework import routers

from .views import inventory_views
from .views  import menu_views

from .viewsets import viewsets

app_name = "api"

router = routers.DefaultRouter()
# app invetory
router.register('ingredient',viewsets.IngredientViewSet)
router.register('item', viewsets.ItemtViewSet)
router.register('item stock', viewsets.ItemStockViewSet)
router.register('item ingredient', viewsets.ItemIngredientViewSet)
# app menu
router.register('product', viewsets.ProductViewSet)
router.register('category', viewsets.CategoryViewSet)


urlpatterns = [
    path("ingredient/add/", inventory_views.IngredientCreate.as_view(), name="ingredient_app"),
    path("ingredient/update/<int:pk>", inventory_views.IngredientUpdate.as_view(), name="ingredient_update"),
    path("ingredient/", inventory_views.IngredientView.as_view(), name="ingredient_list"),
    path("ingredient/<int:pk>/", inventory_views.IngredientDetailView.as_view(), name="ingredient_detail"),

    path("item/stock/", inventory_views.ItemStockView.as_view(), name="item_stock_list"),
    path("item/stock/<int:pk>/", inventory_views.ItemStockDetailView.as_view(), name="item_stock_detail"),

   
    
    # ITEM
    path("item/<int:pk>/", inventory_views.ItemDetailView.as_view(), name="item_detail"),
    path("item/", inventory_views.ItemView.as_view(), name="item_list"),

    # rotas prontas
    path("item/ingredient/", inventory_views.ItemIngredientView.as_view(), name="item_ingredient_list"),
    path("item/ingredient/<int:pk>/", inventory_views.ItemIngredientDetailView.as_view(), name="item_ingredient_detail"),
    path("item/ingredient/update/<int:pk>", inventory_views.ItemIngredientUpdateView.as_view(), name="item_ingredient_update"),
    path("item/ingredient/delete/<int:pk>", inventory_views.ItemIngredientDeleteView.as_view(), name="item_ingredient_delete"),
    path("item/ingredient/create", inventory_views.ItemIngredientCreateView.as_view() , name="item_ingredient_create"),

    path("product/add/", menu_views.ProductCreateView.as_view(), name="product_create"),
    path("product/", menu_views.ProductListView.as_view(), name="produt_list"),
    path("product/<int:pk>/", menu_views.ProductDetailView.as_view(), name="product_detail"),
    path("product/update/<int:pk>/", menu_views.ProductUpdateView.as_view(), name="product_detail"),
    path("product/delete/<int:pk>/", menu_views.ProductDestroyView.as_view(), name="product_delete"),
    
    path("category/", menu_views.CategoryListView.as_view(), name="category_lsit"),
    path("category/<int:pk>/", menu_views.CategoryDetailView.as_view(), name="category_detail"),
    path("category/update/<int:pk>/", menu_views.CategoryUpdateView.as_view(), name="category_update"),
    path("category/delete/<int:pk>/", menu_views.CategoryDeleteView.as_view(), name="category_delete"),
    path("category/add/", menu_views.CategoryCraateView.as_view(), name="category_create"),

    # essa rota deve esta sempre no final. sim
    path('', include(router.urls)),
]
