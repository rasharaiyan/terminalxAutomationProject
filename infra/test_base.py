import unittest
import json
from selenium import webdriver
import os


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(base_dir, 'tests', 'ui_tests', 'test_config.json')
        # Load the test configuration
        with open(config_path, encoding='utf-8') as config_file:
            cls.config = json.load(config_file)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
