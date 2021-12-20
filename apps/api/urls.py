from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # rotas prontas
    path("ingredient/add/", inventory_views.IngredientCreateView.as_view(), name="ingredient_app"),
    path("ingredient/update/<int:pk>", inventory_views.IngredientUpdateView.as_view(), name="ingredient_update"),
    path("ingredient/<int:pk>/", inventory_views.IngredientDetailView.as_view(), name="ingredient_detail"),
    path("ingredient/", inventory_views.IngredientView.as_view(), name="ingredient_list"),
    path("ingredient/delete/<int:pk>/", inventory_views.IngredientDeleteView.as_view(), name="ingredient_delete"),
    
    path("item/stock/add/", inventory_views.ItemStockCreatelView.as_view(), name="item_stock_create"),
    path("item/stock/", inventory_views.ItemStockView.as_view(), name="item_stock_list"),
    path("item/stock/<int:pk>/", inventory_views.ItemStockDetailView.as_view(), name="item_stock_detail"),
    path("item/stock/update/<int:pk>/", inventory_views.ItemStockUpdateView.as_view(), name="item_stock_update"),
    path("item/stock/delete/<int:pk>/", inventory_views.ItemStockDeleteView.as_view(), name="item_stock_delete"),

    path("item/add/", inventory_views.ItemCreateView.as_view(), name="item_create"),
    path("item/", inventory_views.ItemView.as_view(), name="item_list"),
    path("item/<int:pk>/", inventory_views.ItemDetailView.as_view(), name="item_detail"),
    path("item/delete/<int:pk>/", inventory_views.ItemDeleteView.as_view(), name="item_delete"),
    path("item/update/<int:pk>/", inventory_views.ItemUpdateView.as_view(), name="item_update"),

    path("item/ingredient/add/", inventory_views.ItemIngredientCreateView.as_view() , name="item_ingredient_create"),
    path("item/ingredient/<int:pk>/", inventory_views.ItemIngredientDetailView.as_view(), name="item_ingredient_detail"),
    path("item/ingredient/", inventory_views.ItemIngredientView.as_view(), name="item_ingredient_list"),
    path("item/ingredient/update/<int:pk>/", inventory_views.ItemIngredientUpdateView.as_view(), name="item_ingredient_update"),
    path("item/ingredient/delete/<int:pk>/", inventory_views.ItemIngredientDeleteView.as_view(), name="item_ingredient_delete"),
  
    path("product/add/", menu_views.ProductCreateView.as_view(), name="product_create"),
    path("product/", menu_views.ProductListView.as_view(), name="produt_list"),
    path("product/<int:pk>/", menu_views.ProductDetailView.as_view(), name="product_detail"),
    path("product/update/<int:pk>/", menu_views.ProductUpdateView.as_view(), name="product_detail"),
    path("product/delete/<int:pk>/", menu_views.ProductDestroyView.as_view(), name="product_delete"),
    
    path("category/add/", menu_views.CategoryCreateView.as_view(), name="category_create"),
    path("category/", menu_views.CategoryListView.as_view(), name="category_lsit"),
    path("category/<int:pk>/", menu_views.CategoryDetailView.as_view(), name="category_detail"),
    path("category/update/<int:pk>/", menu_views.CategoryUpdateView.as_view(), name="category_update"),
    path("category/delete/<int:pk>/", menu_views.CategoryDeleteView.as_view(), name="category_delete"),
    
    # essa rota deve esta sempre no final. sim
    path('', include(router.urls)),
]
