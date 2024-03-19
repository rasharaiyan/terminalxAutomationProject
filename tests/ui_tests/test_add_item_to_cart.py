import time
import unittest
from infra.base_page import BasePage
from logic.cart_functionalities import AddToCart
from logic.search_functionality import SearchFunctionality
from infra.test_base import TestBase

class TestAddToCartFunctionality(TestBase):

    def setUp(self):
        super().setUp()
        self.base_page = BasePage(self.driver)
        self.add_to_cart = AddToCart(self.driver)
        self.search_functionality = SearchFunctionality(self.driver)
        self.base_url = self.config['Tests']['baseURL']
        self.search_query = self.config['Tests']['queries'][0]['searchQuery']
        self.expected_item = self.config['Tests']['queries'][0]['expectedResult']

    def test_add_item_to_cart(self):
        try:
            # Navigate to the site
            self.base_page.navigate_to_site(self.base_url)

            # Perform a search
            self.search_functionality.perform_search(self.search_query)

            # Select the first item
            self.add_to_cart.select_item()

            # Select the first available size
            self.add_to_cart.select_first_size()
            time.sleep(5)

            # # Add the item to the cart
            self.add_to_cart.add_to_cart()
            time.sleep(5)

        except Exception as e:
            self.fail(f"Test failed with error: {e}")