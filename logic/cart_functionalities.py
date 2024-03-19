from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class AddToCart:

    ADDTOCARTBUTTON = "//button[@class='tx-link-a btn_nDwA tx-link_29YD btn_1UzJ btn-yellow_2tf3']"
    FIRST_ITEM_BUTTON = "//div[@class='product-list-wrapper_1--3']//ol[@class='product-list_yyTm']/li[5]"
    FIRST_SIZE_BUTTON = '//div[@class="size_1bXM"]//div[@data-test-id="qa-size-item"][1]'
    SHOPPING_CART_ICON ='//a[@class="tx-link-a link_2L32 link-minicart_2nwP tx-link_29YD"]'
    ITEMS_IN_CART = '//div[@class="minicart-inner_3M-B"]'

    def __init__(self, driver):
        self._driver = driver

    def select_item(self):
        # Wait for the first item to be clickable and click it
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_ITEM_BUTTON))
        ).click()

    def select_first_size(self):
        # Scroll to the top of the page
        self._driver.execute_script("window.scrollTo(0, 0);")

        # Wait for the first size to be clickable and click it
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_SIZE_BUTTON))
        ).click()

    def add_to_cart(self):
        # Wait for the add to cart button to be clickable and click it
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.ADDTOCARTBUTTON))
        ).click()

    def click_shopping_cart_icon(self):
        # Click on the shopping cart icon
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.SHOPPING_CART_ICON))
        ).click()

    def update_item_quantity(self):
        # Find the dropdown for quantity
        quantity_dropdown = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//select[@class="select_zdc5 rtl_62yk qty-select_RbvK"]'))
        )

        # Select the second option (index 1) from the dropdown
        Select(quantity_dropdown).select_by_index(1)

    def get_updated_quantity(self):
        try:
            # Click on the shopping cart icon to open the cart window
            self.click_shopping_cart_icon()
            time.sleep(3)  # Add a delay to ensure the cart window is fully loaded

            # Find the dropdown for quantity
            quantity_dropdown = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//select[@class="select_zdc5 rtl_62yk qty-select_RbvK"]'))
            )

            # Get the selected quantity from the dropdown
            selected_option = Select(quantity_dropdown).first_selected_option
            return selected_option.text.strip()

        except Exception as e:
            print(f"Error occurred while getting updated quantity: {e}")
            return None


