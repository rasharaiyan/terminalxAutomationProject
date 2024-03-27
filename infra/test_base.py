import unittest
import json
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options



class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(base_dir, 'tests', 'ui_tests', 'test_config.json')
        # Load the test configuration
        with open(config_path, encoding='utf-8') as config_file:
            cls.config = json.load(config_file)

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
        chrome_options.add_argument("--no-sandbox")  # # Bypass OS security model, MUST BE THE VERY FIRST OPTION
        chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()
