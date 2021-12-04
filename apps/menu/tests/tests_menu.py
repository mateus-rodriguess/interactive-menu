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


@pytest.mark.django_db
class TestModel:
	
	def test_create_category(self):
		category = Category
		assert category.objects.count() == 0
		category.objects.create(name="categoria")
		assert category.objects.count() == 1

	def test_model_display_category(self):
		category = mixer.blend(Category, name="categoria")
		assert str(category) ==  "categoria"

	def test_create_table(self):
		table =  Table
		assert table.objects.count() == 0
		Table.objects.create(number=2, description="descrição", max=4)
		assert table.objects.count() == 1

	def test_model_display_table(self):
		table = mixer.blend(Table, number=5)
		assert str(table) ==  "5"

