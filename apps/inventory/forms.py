from django import forms
from .models import Item, Ingredient, ItemIngredient


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        exclude = ("slug",)

    def save(self, commit: bool = ...):
        return super().save(commit=commit)


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = ("slug",)


class ItemIngredientForm(forms.ModelForm):
    class Meta:
        model = ItemIngredient
        fields = "__all__"

    def save(self, commit: bool = ...):
        return super().save(commit=commit)
