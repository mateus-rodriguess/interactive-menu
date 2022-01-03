import pytest
from django.contrib.auth import get_user_model
from apps.account.models import User

@pytest.fixture
def user_data():
    return {'email': 'test@gmail.com', 'username': 'username', 
            'password1': 'user_pass543', 'password2': 'user_pass543', "CPF": 48684721608}


@pytest.fixture
def user_data_login():
    return {'username': 'username', 'password': 'user_pass543'}


@pytest.fixture
def user(db):
    return User.objects.create(username="teste", password="testes1234")


@pytest.fixture
def create_test_user(user_data_login):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data_login)
    test_user.set_password(user_data_login.get('password'))
    return test_user


@pytest.fixture
def authenticated_user(client, user_data_login):
	user_model = get_user_model()
	test_user = user_model.objects.create_user(**user_data_login)
	test_user.set_password(user_data_login.get('password'))
	test_user.save()
	client.login(**user_data_login)
	return test_user
