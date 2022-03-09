from django.contrib.postgres.search import SearchVector
from django.shortcuts import get_object_or_404, render

from apps.cart.forms import CartAddProductForm
from apps.inventory.models import ItemIngredient, Ingredient

from .forms import SearchForm
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None

    form = SearchForm()
    categories = Category.objects.all()
    products = Product.available_mamager.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if "search_form" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Product.available_mamager.annotate(
                search=SearchVector('name', 'description')).filter(search=query)

    return render(request, 'menu/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products, 'form': form})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    ingredient = Ingredient.objects.filter(id=product.ingredient.pk).first()
    item_ingredient = ItemIngredient.objects.filter(ingredient=ingredient)

    cart_product_form = CartAddProductForm()

    return render(request,
                  'menu/product/detail.html',
                  {'product': product, "item_ingredient": item_ingredient, "ingredient": ingredient,
                   'cart_product_form': cart_product_form})
