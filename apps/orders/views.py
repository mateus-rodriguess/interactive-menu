from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order


@login_required
def order_create(request):
    cart = Cart(request)

    if not cart:
        return redirect('menu:product_list')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task

            return redirect('orders:order_list')

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user, paid=False)
    orde_list = []
    price_total = 0
    for order in orders:
        orderitem = OrderItem.objects.filter(order=order).last()

        price_total += orderitem.quantity * orderitem.price

        orde_list.append(orderitem)

    return render(request, "orders/list.html", {"orderitem": orde_list, "orders": orders, "price_total": price_total})
