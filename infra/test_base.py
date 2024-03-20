import unittest
import json
from selenium import webdriver
import os


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Construct the path to the test configuration file relative to this script
        config_path = os.path.join(os.path.dirname(__file__), 'test_config.json')
        # Load the test configuration
        with open(config_path, encoding='utf-8') as config_file:
            cls.config = json.load(config_file)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
