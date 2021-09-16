from django import forms
from django.forms import fields
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'