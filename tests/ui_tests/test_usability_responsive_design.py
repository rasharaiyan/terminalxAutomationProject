from infra.test_base import TestBase
from logic.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestResponsiveDesign(TestBase):

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)

    def test_responsive_design(self):
        self.home_page.navigate_to_site(self.config['Tests']['baseURL'])

        # Iterate over the screen sizes from the configuration file
        for size in self.config['Tests']['screenSizes']:
            self.driver.set_window_size(size['width'], size['height'])
            time.sleep(3)  # Allow time for the page layout to adjust

            self.assertTrue(self.home_page.is_wishlist_cart_icon_visible(),
                            f'Shopping cart icon not visible at {size}')