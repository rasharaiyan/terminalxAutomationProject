from selenium.webdriver.common.by import By
from infra.test_base import TestBase
from logic.search_functionality import SearchFunctionality
from infra.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from jirareport import JiraReport

class TestPriceSorting(TestBase):

    def setUp(self):
        super().setUp()
        self.test_passed = True  # Initialize test_passed flag as True
        self.search_functionality = SearchFunctionality(self.driver)
        self.base_page = BasePage(self.driver)
        self.base_url = self.config['Tests']['baseURL']
        self.search_item = "Tommy Jeans"

    def convert_price_to_float(self, price_str):
        cleaned_price = ''.join(c for c in price_str if c.isdigit() or c == '.')
        return float(cleaned_price)

    def test_sort_price_low_to_high(self):
        # Navigate to the site and perform search
        self.base_page.navigate_to_site(self.base_url)
        self.search_functionality.perform_search(self.search_item)
        time.sleep(3)

        # Click on sort button and select lowest price to highest
        sort_button = self.driver.find_element(By.XPATH,
                                               "//div[@class='listing-main_byCk']//div[@class='sortby-white_3sWp rtl_1Wy3']")
        sort_button.click()
        lowest_price_to_highest_button = self.driver.find_element(By.XPATH, "//option[@value='price_asc']")
        lowest_price_to_highest_button.click()

        # Wait for elements to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//div[@class='listing-content_2Leu']//div[contains(@class, 'final-price_8CiX')])[1]"))
        )

        # Get prices of the first and second items
        first_item_price = self.driver.find_element(By.XPATH,
                                                    '(//div[@class="listing-content_2Leu"]//div[contains(@class, "final-price_8CiX")])[1]').text
        second_item_price = self.driver.find_element(By.XPATH,
                                                     '(//div[@class="listing-content_2Leu"]//div[contains(@class, "final-price_8CiX")])[2]').text

        # Scroll down to load more items
        self.driver.execute_script("window.scrollBy(0, 800);")

        # Convert prices to float
        first_price = self.convert_price_to_float(first_item_price)
        second_price = self.convert_price_to_float(second_item_price)

        time.sleep(3)

        # Assert that the first item price is lower than the second item price
        try:
            self.assertTrue(first_price > second_price,
                            f"First item price {first_price} is not lower than or equal to second item price {second_price}.")
        except AssertionError:
            # Assertion failed, test will fail, but create Jira issue in tearDown
            self.test_passed = False

    def tearDown(self):
        super().tearDown()  # Call the tearDown method of the parent class
        try:
            if not self.test_passed:
                # Assertion failed, create Jira issue
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure or error"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
        except Exception as e:
            print("Failed to report bug to Jira:", str(e))