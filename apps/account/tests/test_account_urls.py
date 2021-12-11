from django import urls
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize('param',[
    ('account:login')])
def test_render_views(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 200
  

@pytest.mark.django_db
@pytest.mark.parametrize('param',[
    ('account:logout')])
def test_rendirect_url_logout(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 302