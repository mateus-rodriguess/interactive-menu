from django import forms
from .models import Item, Ingredient, ItemIngredient


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = "__all__"

    def save(self, commit: bool = ...):
        return super().save(commit=commit)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = "__all__"


class ItemIngredientForm(forms.ModelForm):
    class Meta:
        model = ItemIngredient
        fields = "__all__"

    def save(self, commit: bool = ...):
        return super().save(commit=commit)
