from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings

from store.models import Product
from .basket import Basket

from django_htmx.http import trigger_client_event

def basket_summary(request):
    context = {}
    return render(request, 'store/basket/summary.html', context)


@require_http_methods(["PUT", "POST"])
def add_to_basket(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.add(product=product)
    response = render(request, 'store/products/_added2basketalready.html')
    trigger_client_event(response, "basketUpdatedEvent", { },)
    return response

@require_http_methods(["DELETE", "POST"])
def remove_from_basket(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.delete(product=product)
    response = HttpResponse()
    trigger_client_event(response, "basketUpdatedEvent", { },)
    return response


def update_basket_details(request):
    return render(request, 'store/basket/_details.html')

def update_basket_number(request):
    # basket = Basket(request)
    return render(request, 'store/basket/_number.html')


def update_basket_footer(request):
    # basket = Basket(request)
    return render(request, 'store/basket/_footer.html')
