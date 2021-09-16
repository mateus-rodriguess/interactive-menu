from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItem
from .forms import OrderCreateForm
from apps.cart.cart import Cart

# Create your views here.

@login_required
def order_create(request):
    cart = Cart(request)
  
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            print("aqui")
            order = form.save(user=request.user)

            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])
            
            cart.clear()
            return render(request, 'orders/order/created.html',{'order': order})
        
        else:
            form = OrderCreateForm()
           
            return render(request,'orders/order/create.html',{'cart': cart, 'form': form})