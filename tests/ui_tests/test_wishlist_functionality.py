import unittest
import time
from infra.base_page import BasePage
from logic.search_functionality import SearchFunctionality
from logic.wish_list_functionality import WishlistFunctionality
from infra.test_base import TestBase

class TestWishlistFunctionality(TestBase):

    def setUp(self):
        super().setUp()
        self.base_page = BasePage(self.driver)
        self.search_functionality = SearchFunctionality(self.driver)
        self.wishlist_functionality = WishlistFunctionality(self.driver)
        self.base_url = self.config['Tests']['baseURL']
        self.search_query = self.config['Tests']['queries'][0]['searchQuery']

    def test_add_item_to_wishlist(self):
        self.base_page.navigate_to_site(self.base_url)
        self.search_functionality.perform_search(self.search_query)
        self.wishlist_functionality.add_first_item_to_wishlist()
        time.sleep(5)
        self.assertTrue(self.wishlist_functionality.is_item_in_wishlist(), "Item was not added to the wishlist.")