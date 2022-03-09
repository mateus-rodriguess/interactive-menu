from rest_framework.permissions import BasePermission
from apps.account.models import User

class Permission_atk(BasePermission):
    def has_object_permission(self, request, view, obj):
        # fazer uma logica pra permitir so adm aqui 
        return obj.User.filter(is_staff=True).exists()