from django import forms
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import UserCreationFormCustom, ProfileEditForm
from .models import Profile


class CreateUser(generic.CreateView):
    """
    view that reder the template for user registration
    """

    def get_queryset(self):
        return self.request.user

    form_class = UserCreationFormCustom
    template_name = 'registration/register.html'
    # alterar o redirect
    success_url = reverse_lazy('account:login')


@login_required()
def ProfileDetailView(request, slug):
    """
    user profile view
    """  
    return render(request, "profile/profile.html")


@login_required
def edit_prifile(request, slug):

    print(slug)

    profile = Profile.objects.get(user=request.user.id)
    print(profile)
    if request.method == 'POST':
        print("ok")
        profile_form = ProfileEditForm(instance=request.user, data=request.POST)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileEditForm()
    return render(request,'profile/edit.html',{'profile_form': profile_form})
