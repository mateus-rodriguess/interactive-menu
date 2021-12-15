from rest_framework.permissions import BasePermission


class Permission_atk(BasePermission):
    def has_object_permission(self, request, view, obj):
        # fazer uma logica pra permitir so adm aqui 
        print("# fazer uma logica pra permitir so adm aqui ")
        return obj.Ingredient.filter(id=100).exists()