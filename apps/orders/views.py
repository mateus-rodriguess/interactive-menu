from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.cart.cart import Cart
from apps.account.models import Profile
from .forms import OrderCreateForm
from .models import OrderItem

# Create your views here.

@login_required
def order_create(request):
    cart = Cart(request)
    
    if not cart:
        # url passa mal
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
           
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
