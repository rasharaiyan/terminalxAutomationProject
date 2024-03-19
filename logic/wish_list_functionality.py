from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WishlistFunctionality:

    FIRST_ITEM_ADD_TO_WISHLIST_BUTTON_XPATH = "//div[@class='product-list-wrapper_1--3']//ol[@class='product-list_yyTm']/li[1]"
    WISHLIST_INDICATOR_XPATH = "//*[@id='app-root']/div[2]/main/div[2]/div/div/div[2]/div[1]/div[2]/div/div[6]/button"

    def __init__(self, driver):
        self._driver = driver

    def add_first_item_to_wishlist(self):
        add_to_wishlist_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_ITEM_ADD_TO_WISHLIST_BUTTON_XPATH))
        )

        self._driver.execute_script("arguments[0].scrollIntoView(true);", add_to_wishlist_button)
        time.sleep(2)  # Pause to ensure the scroll effect is observed

        # Highlight the add to wishlist button
        self._driver.execute_script("arguments[0].setAttribute('style', 'border: 4px solid red;');",
                                    add_to_wishlist_button)
        time.sleep(2)
        # Click the add to wishlist button
        add_to_wishlist_button.click()
        time.sleep(2)  # Add a small delay to observe the action

        # Re-locate the wishlist button element
        wishlist_section = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.WISHLIST_INDICATOR_XPATH))
        )

        # Scroll to the wishlist button using JavaScript
        self._driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - 100);",
                                    wishlist_section)
        time.sleep(2)

        # Click on the wishlist button
        wishlist_section.click()
        time.sleep(2)  # Pause to observe the action

    def is_item_in_wishlist(self):
        # Wait for the wishlist indicator to be visible and check its text
        wishlist_indicator = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.WISHLIST_INDICATOR_XPATH))
        )
        return wishlist_indicator.text != "0"
