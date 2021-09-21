from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
   
    note = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Order
        fields = ['table', 'note']