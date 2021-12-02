from django import urls
from django.contrib.auth import get_user_model
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


@pytest.mark.django_db
def test_user_create_user(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    create_user_url = urls.reverse("account:register")
    resp = client.post(create_user_url, user_data)
    assert user_model.objects.count() == 1
    assert resp.status_code ==  302


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data_login):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse("account:login")
    resp = client.post(login_url, data=user_data_login)
 
    assert resp.status_code == 302
    assert resp.url == urls.reverse('menu:product_list')


@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
	logout_url = urls.reverse('account:logout')
	resp = client.get(logout_url)
	assert resp.status_code == 302
	assert resp.url == urls.reverse('menu:product_list')