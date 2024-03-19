from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class BasePage():

    def __init__(self, driver):
        self._driver = driver

    def navigate_to_site(self, url):
        self._driver.get(url)

    def get_url_driver(self):
        return self._driver.current_url

    def scroll_down(self):
        # Execute JavaScript to scroll down the page
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")