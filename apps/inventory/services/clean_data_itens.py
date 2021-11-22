from apps.inventory.models import ItemStock, Item

def save_items_stock(items, quantity, potions, kilos):
    items_list = []
    quantity_list = []
    potions_list = []
    kilos_list = []
    i = 0
    items_list.append(items)
    quantity_list.append(quantity)

    potions_list.append(potions)
    kilos_list.append(kilos)

   
    for item in items_list:
      
        try:
            item_model = Item.objects.get(name=item)
            item_stock = ItemStock.objects.filter(item=item_model).last()
            
            if item_stock: 
                item_stock.quantity -=  quantity_list[i]
                item_stock.potions -=  potions_list[i]
                item_stock.kilos -=  potions_list[i]
                item_stock.save()
                return True
            i += 1
            return False

        except:
            return False
      

    
    

  