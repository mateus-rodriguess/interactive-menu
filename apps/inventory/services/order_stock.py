from apps.orders.models import OrderItem
from apps.menu.models import Product
from apps.inventory.models import ItemStock, Ingredient, ItemIngredient


def stock(order_instance):
    order_item_list = OrderItem.objects.filter(order=order_instance)
    
    for order_item in order_item_list:
      
        product = Product.objects.get(pk=order_item.product.id)
        ingredient = Ingredient.objects.get(pk=product.ingredient.id)
        item_ingredient_list = ItemIngredient.objects.filter(ingredient=ingredient)
        
        for item_ingredient in item_ingredient_list:
         
            item_stock = ItemStock.objects.get(item=item_ingredient.item.id)
            
            if item_stock.quantity >= item_ingredient.quantity * order_item.quantity:
                item_stock.quantity -= item_ingredient.quantity * order_item.quantity
               
                if item_stock.potions >= item_ingredient.potions * order_item.quantity:
                    item_stock.potions -= item_ingredient.potions * order_item.quantity
                else:
                    item_stock.potions = 0
                if item_stock.kilos >= item_ingredient.kilos * order_item.quantity:
                    item_stock.kilos -= item_ingredient.kilos * order_item.quantity
                else:
                    item_stock.kilos = 0
                item_stock.save()
            else: 
                continue
            
    