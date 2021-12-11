from django.contrib.sessions.middleware import SessionMiddleware
from django.http import request
import pytest
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from apps.account.models import User
from apps.menu.models import Product, Category
from apps.cart.views import cart_detail

