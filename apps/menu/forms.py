from django import forms
from .models import Product

class SearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Pesquisar","class":"form-control"}), label="Pesquisar")


class ProductForm(forms.Form):
    
    class Meta:
        model = Product
        exclude = ("slug",)
         

