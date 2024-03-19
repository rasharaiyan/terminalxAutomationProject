from infra.test_base import TestBase
from logic.home_page import HomePage
from infra.base_page import BasePage

class TestColorAccessibility(TestBase):

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.base_page=BasePage(self.driver)
        self.base_url = self.config['Tests']['baseURL']


    def test_color_blindness_feature(self):
        # Navigate to the site
        self.base_page.navigate_to_site(self.base_url)
        # Enable color blindness mode
        self.home_page.enable_color_blindness_mode()
