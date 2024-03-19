from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


class SearchFunctionality:

    SEARCH_BUTTON_XPATH = "//button[@class='search-button_1ENs']"
    SEARCH_INPUT_XPATH = "//input[@class='input_sILM']"
    SEARCH_RESULT_XPATH = "//div[@class='search-results_2YMu']"

    def __init__(self, driver):
        self._driver = driver

    def perform_search(self, query):
        # Wait for the search button to be clickable and click it
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_BUTTON_XPATH))
        ).click()

        # Wait for the search input to be visible
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_INPUT_XPATH))
        )

        # Now that the search input is visible, we can find it and interact with it
        search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT_XPATH)
        search_input.clear()
        search_input.send_keys(query)
        time.sleep(5)  # Pause to visually confirm the input text
        search_input.send_keys(Keys.ENTER)


    def validate_search_results(self, expected_result):
        # Wait for the first search result to be visible
        time.sleep(5)
        first_result = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.SEARCH_RESULT_XPATH))
        )
        return expected_result.lower() in first_result.text.lower()