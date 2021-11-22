from .cart import Cart


def cart(request):
    """
    context processor
    """
    return {'cart': Cart(request)}
