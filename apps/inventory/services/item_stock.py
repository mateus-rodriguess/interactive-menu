from apps.inventory.models import ItemStock, Item

def item_stock_qt(items, quantity, potions, kilos):
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

            if  not quantity_list[i] >=  item_stock.quantity:
                pass
            if  not potions_list[i] >=  item_stock.potions:
                pass
            if  not potions_list[i] >=  item_stock.kilos:
                pass
            return True
        except:
            pass
            
        i += 1

    return True