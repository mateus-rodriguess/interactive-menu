
from apps.inventory.models import ItemStock, Item

def save_items_stock(items, quantity, potions, kilos):
    i = 0
    items_list = []
    quantity_list = []
    potions_list = []
    kilos_list = []
    items_list.append(items.pk)
    quantity_list.append(quantity)

    potions_list.append(potions)
    kilos_list.append(kilos)
    
   
    for item in items_list:  
        item_model = Item.objects.get(pk=item)
        item_stock = ItemStock.objects.filter(item=item_model).last()
 
        if item_stock: 
            item_stock.quantity -=  quantity_list[i]
            item_stock.potions -=  potions_list[i]
            item_stock.kilos -=  potions_list[i]
            item_stock.save()
        i += 1

      

    
    

  