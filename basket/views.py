from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

from store.models import Product


from .basket import Basket

def basket_summary(request):
    context = {}
    return render(request, 'store/basket/summary.html', context)


@require_http_methods(["PUT", "POST"])
def add_to_basket(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.add(product=product, quantity=1)
    response = HttpResponse(f'{len(basket)}')


    # cart = get_or_create_cart(request)
    # cart_items = cart.get_cart_items()

    # product_in_cart = False # firstly we supose that the product has not been added to the cart yet
    # for cart_item in cart_items:
    #     if cart_item.product.id == added_product.id: # then we check if it was already added
    #         product_in_cart = True
    #         response = HttpResponse(f'{added_product.title} is already in your cart')
    # if not product_in_cart:
    #     new_cart_item = Item(cart=cart, product=added_product)
    #     new_cart_item.save()
    return response

@require_http_methods(["DELETE", "POST"])
def remove_from_basket(request, item_id):
    cart = get_or_create_cart(request)
    item = get_object_or_404(Item, id=item_id)
    if item in cart.get_cart_items():
        item.delete()
    return HttpResponse()
