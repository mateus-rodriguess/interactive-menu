from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User
from .forms import UserCreationForm, UserChangeForm, ProfileForm
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','user', 'active']
    form = ProfileForm
    add_form = ProfileForm
    model = Profile

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username','email','CPF', 'is_superuser', 'is_staff', 'is_active',]
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ("CPF", {"fields": ("CPF",)}),
    )
    
