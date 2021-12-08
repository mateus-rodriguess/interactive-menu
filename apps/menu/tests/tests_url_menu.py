from django import urls
from django.urls import reverse, resolve
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('param', [
    ('menu:product_list')])
class TestMenuView():

    def test_product_list(self, client, param):
        temp_url = urls.reverse(param)
        resp = client.get(temp_url)
        assert resp.status_code == 200
	

@pytest.mark.django_db
def test_product_detail_url(product_one):
    path = reverse('menu:product_detail', kwargs={'id':1, "slug": str(product_one)}) 
    assert resolve(path).view_name == "menu:product_detail"
  

@pytest.mark.django_db
def test_product_list_by_category_url(category):
    path = reverse('menu:product_list_by_category', kwargs={"category_slug": str(category)}) 
    assert resolve(path).view_name == "menu:product_list_by_category"
  

  
  