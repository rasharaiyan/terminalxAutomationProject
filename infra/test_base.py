import unittest
import json
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from jira import JIRA


class TestBase(unittest.TestCase):
    TOKEN = 'ATATT3xFfGF0APBsKmZR8f7eDdkbbVNoE-b_pO2XSUspFVt64RYLq_A4S-yGcjA8D8710Sg3JcTg7jBUm-j9wiXcFK3aW4b3ylnSdlNMhKzm1ZGX7LtEY7zRZUu_Ad86Wh3zSGaizCQrDLxHFrAG3RsvsweDaW4ML3GXknFV-mdSY6py9OFgWu4=630E0F2B'
    jira_url = 'https://rasharaiyanbd24.atlassian.net/'
    auth_jira = JIRA(basic_auth=('rasharaiyan00@gmail.com', TOKEN), options={'server': jira_url})
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

    def create_issue(self, summary, description, project_key, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': f'failed test: {summary}',
            'description': description,
            'issuetype': {'name': issue_type},
        }
        new_issue = self.auth_jira.create_issue(fields=issue_dict)
        return new_issue.key
