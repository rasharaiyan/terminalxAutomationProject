import unittest
import json
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from jirareport import JiraReport


class APITestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(base_dir, 'tests', 'api_tests', 'test_config.json')
        # Load the test configuration
        with open(config_path, encoding='utf-8') as config_file:
            cls.config = json.load(config_file)


    def report_jira_issue(self, summary, description):
        try:
            jira_report = JiraReport()
            jira_report.create_issue(summary, description)
            print("Issue Created")
        except Exception as e:
            print("Failed to report bug to Jira:", str(e))
