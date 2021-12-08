from django.contrib.sessions.middleware import SessionMiddleware

import pytest
from apps.menu.views import product_detail, product_list
from apps.menu.models import Product, Category
from apps.account.models import User
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestViewsMenu:
    request = None

    def setUp(self, path):
        # add session a request
        self.middleware = SessionMiddleware(path)
        self.request = RequestFactory().get(path)
        self.middleware.process_request(self.request)
        self.request.session.save()

    def test_product_detail_is_authenticated(self, ingredient):
        # msm sem ta logoda e permitido ver esse view
        category = mixer.blend(Category, name="pizza", slug="pizza")
        product = mixer.blend(Product, name="pizza", slug="pizza",
                              price=2.9, ingredient=ingredient, category=category)
        path = reverse('menu:product_detail', kwargs={
                       'id': product.id, "slug": product.slug})

        self.setUp(path)
        self.request.user = mixer.blend(User)

        response = product_detail(
            self.request, id=product.id, slug=product.slug)
        assert response.status_code == 200

    def test_product_list_view(self, ingredient):
        category = mixer.blend(Category, name="pizza", slug="pizza")
        product = mixer.blend(Product, name="pizza", slug="pizza",
                              price=2.9, ingredient=ingredient, category=category)
        path = reverse('menu:product_list')
        self.setUp(path)

        self.request.user = mixer.blend(User)
        response = product_list(self.request)

        assert response.status_code == 200
        assert product.name in str(
            response.content) and category.name in str(response.content)
