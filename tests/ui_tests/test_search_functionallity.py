import time
import unittest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from infra.base_page import BasePage
from logic.search_functionality import SearchFunctionality
from selenium.webdriver.support import expected_conditions as EC
from infra.test_base import TestBase


class TestSearchFunctionality(TestBase):

    def setUp(self):
        super().setUp()
        self.base_page = BasePage(self.driver)
        self.search_functionality = SearchFunctionality(self.driver)
        self.base_url = self.config['Tests']['baseURL']
        self.search_query = self.config['Tests']['queries'][0]['searchQuery']
        self.expected_result = self.config['Tests']['queries'][0]['expectedResult']

    def test_search_functionality(self):
        # Navigate to the website and wait for it to be fully loaded
        self.base_page.navigate_to_site(self.base_url)
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located)

        # Perform search and validate results
        self.search_functionality.perform_search(self.search_query)
        result = self.search_functionality.validate_search_results(self.expected_result)
        self.assertTrue(result, "Search results are not relevant.")