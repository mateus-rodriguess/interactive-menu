from django import forms
from .models import Item, Revenue, ItemRevenue
from apps.inventory.services.clean_data_itens import save_items_stock
from apps.inventory.services.item_stock import item_stock_qt

class RevenueForm(forms.ModelForm):
    
    class Meta:
        model = Revenue
        exclude = ("slug",)
    
    
    def save(self, commit: bool = ...):
        # possivel alteração    
        return super().save(commit=commit)

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        exclude =  ("slug",)


class ItemRevenueForm(forms.ModelForm):
    class Meta:
        model = ItemRevenue
        fields =  "__all__"

    def clean(self):
        cd = self.cleaned_data
        self.items = self.cleaned_data['item']
        self.quantity = self.cleaned_data['quantity']
        self.potions = self.cleaned_data['potions']
        self.kilos = self.cleaned_data['kilos']

        if not item_stock_qt(self.items, self.quantity, self.potions, self.kilos):
            self.add_error('item', "item insuficiente nenhum estoque")
        return cd
    
    def save(self, commit: bool = ...):
        
        if save_items_stock(self.items, self.quantity, self.potions, self.kilos):
            return super().save(commit=commit)    
   

  

   


