from apps.orders.models import Order, OrderItem
from apps.menu.models import Product
from apps.inventory.models import ItemStock, Revenue, ItemRevenue

def stock(order_instance):
    order_item = OrderItem.objects.filter(order=order_instance)
       
    for item_list in  order_item:
        # fazer tratamento de erros possiveis 
        product = Product.objects.get(pk=item_list.product.id)
        revenue =  Revenue.objects.get(pk=product.revenue.id)
        item_revenue =  ItemRevenue.objects.filter(revenue=revenue).last()
        
        if item_revenue:
            item_stock = ItemStock.objects.filter(item=item_revenue.item.id).last()
            item_stock.quantity -=  item_revenue.quantity
            item_stock.potions -=  item_revenue.potions
            item_stock.kilos -=  item_revenue.kilos
            item_stock.save()