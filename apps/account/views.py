from apps.menu.models import Product
from django import forms
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm, ProfileForm
from .models import Profile, User
from apps.orders.views import order_list


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
    profile = Profile.objects.get(user=request.user)
    orders = order_list(request)

    note = orders[0]['order']
    product = orders[0]['orderitem']
 
    return render(request, "profile/profile.html", {"profile": profile, 'note': note, "product": product})


@login_required
def edit_profile(request, slug):

    try:
        profile = Profile.objects.get(user=request.user)    
    except Exception as e:
        print(e)
        return render(request,'profile/not_found.html')
   
    if  not request.user.username == slug:
        return redirect("account:login")

    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()
            return redirect("account:profile-detail-view", slug)
    else:
        profile_form = ProfileForm()
    return render(request,'profile/edit.html',{'profile_form': profile_form})
