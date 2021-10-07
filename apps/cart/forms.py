from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 14)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int, widget=forms.Select(attrs={"class": "custom-select"}))
    override = forms.BooleanField(required=False,
                                  widget=forms.HiddenInput(attrs={"class": "btn btn-primary"}))