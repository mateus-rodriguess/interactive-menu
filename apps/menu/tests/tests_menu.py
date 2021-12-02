from django import urls
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('param',[
    ('menu:product_list')])
def test_manu_list_view(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 200