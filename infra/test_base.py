import unittest
import json
from selenium import webdriver

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load the test configuration
        with open('/tests/ui_tests/test_config.json', encoding='utf-8') as config_file:
            cls.config = json.load(config_file)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
