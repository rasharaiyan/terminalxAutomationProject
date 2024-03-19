from selenium.webdriver.common.by import By
from infra.test_base import TestBase
from logic.search_functionality import SearchFunctionality
from infra.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestPriceSorting(TestBase):

    def setUp(self):
        super().setUp()
        self.search_functionality = SearchFunctionality(self.driver)
        self.base_page = BasePage(self.driver)
        self.base_url = self.config['Tests']['baseURL']
        self.search_item = "Tommy Jeans"

    def convert_price_to_float(self, price_str):
        cleaned_price = ''.join(c for c in price_str if c.isdigit() or c == '.')
        return float(cleaned_price)

    def test_sort_price_low_to_high(self):
        self.base_page.navigate_to_site(self.base_url)
        self.search_functionality.perform_search(self.search_item)
        time.sleep(3)
        sort_button = self.driver.find_element(By.XPATH, "//div[@class='listing-main_byCk']//div[@class='sortby-white_3sWp rtl_1Wy3']")
        sort_button.click()
        lowest_price_to_highest_button = self.driver.find_element(By.XPATH, "//option[@value='price_asc']")
        lowest_price_to_highest_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@class='listing-content_2Leu']//div[contains(@class, 'final-price_8CiX')])[1]"))
        )

        first_item_price = self.driver.find_element(By.XPATH, '(//div[@class="listing-content_2Leu"]//div[contains(@class, "final-price_8CiX")])[1]').text
        second_item_price = self.driver.find_element(By.XPATH, '(//div[@class="listing-content_2Leu"]//div[contains(@class, "final-price_8CiX")])[2]').text

        first_price = self.convert_price_to_float(first_item_price)
        second_price = self.convert_price_to_float(second_item_price)

        time.sleep(3)

        self.assertTrue(first_price <= second_price,
                        f"First item price {first_price} is not lower than or equal to second item price {second_price}.")