from django.urls import reverse, resolve
import pytest


@pytest.mark.django_db
def test_order_create_url(order, client):
    path = reverse("orders:order_create")
    response = client.get(path)
    assert response.status_code == 302
    assert resolve(path).view_name == "orders:order_create"


@pytest.mark.django_db
def test_order_list_url(order, client):
    path = reverse("orders:order_list")
    response = client.get(path)
    assert response.status_code == 302
    assert resolve(path).view_name == "orders:order_list"