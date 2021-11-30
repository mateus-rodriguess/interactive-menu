from apps.orders.models import OrderItem
from apps.menu.models import Product
from apps.inventory.models import ItemStock, Revenue, ItemRevenue

def stock(order_instance):
 
    order_item_list = OrderItem.objects.filter(order=order_instance)
    
    for order_item in  order_item_list:
      
        product = Product.objects.get(pk=order_item.product.id)
        revenue =  Revenue.objects.get(pk=product.revenue.id)
        item_revenue_list =  ItemRevenue.objects.filter(revenue=revenue)
        
        for item_revenue in item_revenue_list:
         
            item_stock = ItemStock.objects.get(item=item_revenue.item.id)
            
            if  item_stock.quantity >= item_revenue.quantity * order_item.quantity:
                item_stock.quantity -=  item_revenue.quantity * order_item.quantity
               
                if item_stock.potions >= item_revenue.potions * order_item.quantity: 
                    item_stock.potions -=  item_revenue.potions * order_item.quantity
                else:
                    item_stock.potions = 0
                if item_stock.kilos >=  item_revenue.kilos * order_item.quantity:
                    item_stock.kilos -=  item_revenue.kilos * order_item.quantity
                else:
                    item_stock.kilos = 0
                print(item_revenue)
                item_stock.save()
            else: 
                continue
            
    