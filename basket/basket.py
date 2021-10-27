from decimal import Decimal

from django.conf import settings
from store.models import Product


class Basket():
    """
    A base basket class, providing some default behaviours that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {}

        self.basket = basket

    def add(self, product, quantity=1):
        """
        Adding and updating the users basket session data
        """
        product_id_str =  str(product.id)

        if product_id_str in self.basket:
            self.basket[product_id_str]["quantity"] = quantity
        else:
            self.basket[product_id_str] = {"price": str(product.price), "quantity": quantity}

        self.save()

    def delete(self, product):
        """
        Deleting the users basket session data
        """
        product_id_str = str(product.id)

        if product_id_str in self.basket:
            del self.basket[product_id_str]
            self.save()



    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item


    def __len__(self):
        """
        Get the basket data and count the quantity of items
        """
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) *item['quantity'] for item in self.basket.values())

    def save(self):
            self.session.modified = True
