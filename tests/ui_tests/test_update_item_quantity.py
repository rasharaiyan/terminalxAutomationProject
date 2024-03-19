import time
import unittest
from infra.base_page import BasePage
from logic.cart_functionalities import AddToCart
from logic.search_functionality import SearchFunctionality
from infra.test_base import TestBase
from selenium.common.exceptions import TimeoutException


class TestUpdateCartFunctionality(TestBase):
    def setUp(self):
        super().setUp()
        self.base_page = BasePage(self.driver)
        self.add_to_cart = AddToCart(self.driver)
        self.search_functionality = SearchFunctionality(self.driver)
        self.base_url = self.config['Tests']['baseURL']
        self.search_query = self.config['Tests']['queries'][0]['searchQuery']
        self.expected_item = self.config['Tests']['queries'][0]['expectedResult']

    def test_update_item_quantity(self):
        try:
            # Navigate to the site
            self.base_page.navigate_to_site(self.base_url)

            # Perform a search
            self.search_functionality.perform_search(self.search_query)

            # Select item from the results list
            self.add_to_cart.select_item()

            # Select the first available size
            self.add_to_cart.select_first_size()
            time.sleep(5)  # Add a delay to ensure the size is selected

            # Add the item to the cart
            self.add_to_cart.add_to_cart()
            time.sleep(5)  # Add a delay to ensure the item is added to the cart

            # Click on the shopping cart icon to open the cart window
            self.add_to_cart.click_shopping_cart_icon()
            time.sleep(3)  # Add a delay to ensure the cart window is fully loaded

            # Update the quantity of the item
            self.add_to_cart.update_item_quantity()
            time.sleep(5)  # Add a delay to observe the change

            # Assert that the item quantity has been updated to 2
            updated_quantity = self.add_to_cart.get_updated_quantity()
            expected_quantity = '2'
            self.assertEqual(updated_quantity, expected_quantity,
                             f"Item quantity not updated correctly. Expected: {expected_quantity}, Actual: {updated_quantity}")

        except TimeoutException:
            self.fail("Timeout occurred while waiting for element to be clickable.")
        except Exception as e:
            self.fail(f"Test failed with error: {e}")

