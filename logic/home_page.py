from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart_and_wishlist_icons_xpath = "//div[@class='cart-and-wishlist_3PHw']"
        self.accessibility_button = "//button[@id='INDmenu-btn']"
        self.color_blindness = "//div[@id='accProfileSection_2']"
        self.checkbox_input = "//input[@id='INDcolorBlindnessSwitchInput']"
        self.close_accessibility_button = "//button[@id='INDcloseAccMenu']"
        self.cart_item_count = '//*[@id="app-root"]/div[2]/header/div/div[2]/div[3]/div/a[2]/span'
        self.cart_icon_to_view_cart = '//a[@class="tx-link-a link_2L32 link-minicart_2nwP tx-link_29YD"]'
        self.loader_visibility = '//div[contains(@class,"loader-container")]'
        self.cart_item_not_found = '//span[text()="סל הקניות שלך ריק."]'

    def navigate_to_site(self, url):
        self.driver.get(url)
        # Wait for the whole page to load
        WebDriverWait(self.driver, 20).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def is_wishlist_cart_icon_visible(self):
        wishlist_cart_icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.shopping_cart_and_wishlist_icons_xpath))
        )
        return wishlist_cart_icon.is_displayed()

    def enable_color_blindness_mode(self):
        # Open accessibility menu
        accessibility_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.accessibility_button))
        )
        accessibility_button.click()

        # Pause for observation
        time.sleep(5)

        # Open color blindness section
        color_blindness_section = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.color_blindness))
        )
        color_blindness_section.click()

        # Pause for observation
        time.sleep(5)

        # Switch to the default content in case the checkbox is inside an iframe
        self.driver.switch_to.default_content()

        # Wait for the checkbox to be present inside the color blindness section
        checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.checkbox_input))
        )

        # Check if the checkbox is already selected
        if not checkbox.is_selected():
            # Click the checkbox only if it's not selected
            checkbox.click()

        # Close the accessibility window
        close_accessibility_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_accessibility_button))
        )
        close_accessibility_button.click()
        time.sleep(2)

    def cart_icon(self):
        cart_item_count = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_item_count))
        )
        return cart_item_count.text

    def cart_empty_message(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element((By.XPATH, self.loader_visibility))
        )
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_icon_to_view_cart))
        ).click()
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_item_not_found))
        ).is_displayed()
