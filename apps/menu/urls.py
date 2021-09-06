from django.urls import path
from .views import index

# urls
urlpatterns = [
   path('', index, name="register"),
]
