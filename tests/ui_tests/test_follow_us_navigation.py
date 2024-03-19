import time
from logic.follow_us import FollowUs
from infra.test_base import TestBase

class TestFollowUsNavigation(TestBase):

    def setUp(self):
        super().setUp()  # Calls the setup from TestBase
        self.follow_us_page = FollowUs(self.driver)
        # using baseURL from the config file:
        self.base_url = self.config['Tests']['baseURL']

    def test_instagram_navigation(self):
        # Navigate to the website and interact with elements
        self.follow_us_page.navigate_to_site(self.base_url)
        time.sleep(5)
        self.follow_us_page.navigate_to_follow_us()
        self.follow_us_page.click_instagram_icon()
        expected_url_substring = "https://www.instagram.com/terminalx/"
        self.assertIn(expected_url_substring, self.follow_us_page.get_url_driver(), "Instagram page URL is incorrect.")

    def test_facebook_navigation(self):
        # Navigate to the website and interact with elements
        self.follow_us_page.navigate_to_site(self.base_url)
        self.follow_us_page.navigate_to_follow_us()
        self.follow_us_page.click_facebook_icon()
        expected_url_substring = "https://www.facebook.com/WEARETERMINALX/"
        self.assertIn(expected_url_substring, self.follow_us_page.get_url_driver(), "Facebook page URL is incorrect.")

    def test_youtube_navigation(self):
        # Navigate to the website and interact with elements
        self.follow_us_page.navigate_to_site(self.base_url)
        self.follow_us_page.navigate_to_follow_us()
        self.follow_us_page.click_youtube_icon()
        expected_url_substring = "https://www.youtube.com/channel/UCUTXP6iS-VyE1Vxllg_3W5g?view_as=subscriber"
        self.assertIn(expected_url_substring, self.follow_us_page.get_url_driver(), "Youtube page URL is incorrect.")
