from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    note = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False)

    class Meta:
        model = Order
        fields = ['note']