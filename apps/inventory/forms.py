from django import forms
from .models import Item, Revenue, ItemRevenue
from apps.inventory.services.clean_data_itens import save_items_stock

class RevenueForm(forms.ModelForm):
    
    class Meta:
        model = Revenue
        exclude = ("slug",)


class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        exclude =  ("slug",)


class ItemRevenueForm(forms.ModelForm):
    class Meta:
        model = ItemRevenue
        fields =  "__all__"

    def save(self, commit: bool = ...):
      
        items = self.cleaned_data['item']
        quantity = self.cleaned_data['quantity']
        potions = self.cleaned_data['potions']
        kilos = self.cleaned_data['kilos']

        
        if save_items_stock(items, quantity, potions, kilos):
            return super().save(commit=commit)
        else:
            print("errro")
            return super().save(commit=commit)


