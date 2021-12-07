from django import urls
import pytest
from mixer.backend.django import mixer
from apps.menu.models import Category, Table


@pytest.mark.django_db
@pytest.mark.parametrize('param',[
    ('menu:product_list')])
class TestMenu:
	
	def test_manu_list_view(self, client, param):
		temp_url = urls.reverse(param)
		resp = client.get(temp_url)
		assert resp.status_code == 200


