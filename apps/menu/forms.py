from django import forms
from django.db.models import query


class SearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder":"Pesquisar","class":"form-control"}), label="Pesquisar")