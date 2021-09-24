from django import forms
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm, ProfileForm
from .models import Profile


class CreateUser(generic.CreateView):
    """
    view that reder the template for user registration
    """
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    
    # alterar o redirect
    success_url = reverse_lazy('menu:product_list')


@login_required()
def ProfileDetailView(request, slug):
    """
    user profile view
    """  
    return render(request, "profile/profile.html")


@login_required
def edit_prifile(request, slug):

    profile = Profile.objects.get(user=request.user)    
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()
            return redirect('menu:product_list')
    else:
        profile_form = ProfileForm()
    return render(request,'profile/edit.html',{'profile_form': profile_form})
