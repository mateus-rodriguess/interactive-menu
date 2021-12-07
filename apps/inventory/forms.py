from django import forms
from .models import Item, Revenue, ItemRevenue


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
 
    def save(self, commit: bool = ...):
        return super().save(commit=commit)  

  

   


