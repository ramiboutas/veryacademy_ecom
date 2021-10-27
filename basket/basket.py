
class Basket():
    """
    A base Basket class, providing some default behaviours that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number': 1231234}

        self.basket = basket

    def add(self, product, quantity):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]["quantity"] = quantity
        else:
            self.basket[product_id] = {"price": str(product.price), "quantity": quantity}

        self.save()

    def __len__(self):
        """
        Get the basket data and count the quantity of items
        """
        print(self.basket)
        print(self.basket.values())

        return sum(item['quantity'] for item in self.basket.values())

    def save(self):
            self.session.modified = True
