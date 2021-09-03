from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateUser

# urls
urlpatterns = [
   path('register/', CreateUser.as_view(), name="register"),
   path('login/', auth_views.LoginView.as_view(), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset")
]
