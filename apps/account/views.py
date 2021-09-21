from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import request
from .forms import UserCreationFormCustom
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


class CreateUser(generic.CreateView):
    """
    view that reder the template for user registration
    """
    def get_queryset(self):
        return self.request.user

    form_class = UserCreationFormCustom
    template_name = 'registration/register.html'
    # alterar o redirect
    success_url = reverse_lazy('login')



@login_required()
def ProfileDetailView(request, slug):
    """
    user profile view
    """
    return render(request, "profile/profile.html")

