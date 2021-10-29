from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

## views:

class TestBasketView(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='myuser')

        ## see more on github from Very Academy!

    def test_basket_url(self):
        """
        Test homepase response status
        """
        response = self.client.get(reverse('basket:summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding an item to the basket
        """
        pass

        ## with htmx is bit more complicated. first learn more about htmx !
