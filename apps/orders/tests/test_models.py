import pytest
from mixer.backend.django import mixer
from apps.orders.models import Order,  OrderItem


@pytest.mark.django_db
def test_order_model(user):
    order = mixer.blend(Order,user=user, paid=False, status="CON", note="ok")
    assert order.user.pk == user.pk and not order.paid and order.status == "CON"

def test_order_item(order, user):
    order_item = mixer.blend(OrderItem, order=order)
    print(order.pk)

    assert order_item.order.pk == order.pk

def test_update_order(order):
    order.paid = True
    order.status = "CON"
    order.save()
    assert order.paid == True and  order.status == "CON"


def test_update_order(order_item):
    order_item.status = "NAC"
    order_item.quantity = 10 
    order_item.save()
    assert order_item.status == "NAC" and  order_item.quantity == 10