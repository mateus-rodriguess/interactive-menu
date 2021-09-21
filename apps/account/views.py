from .forms import UserCreationFormCustom
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


class CreateUser(generic.CreateView):
    """
    view that reder the template for user registration
    """
    form_class = UserCreationFormCustom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile-detail-view')



@login_required()
def ProfileDetailView(request, slug):
    """
    user profile view
    """
    return render(request, "profile/profile.html")

