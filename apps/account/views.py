from .forms import UserCreationFormCustom
from django.urls import reverse_lazy
from django.views import generic


class CreateUser(generic.CreateView):
    """
    view that reder the template for user registration
    """
    form_class = UserCreationFormCustom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


