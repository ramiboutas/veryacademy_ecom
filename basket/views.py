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
    basket.add(product=product)
    return HttpResponse(f'{basket.__len__()}')

@require_http_methods(["DELETE", "POST"])
def remove_from_basket(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.delete(product=product)
    return HttpResponse()
