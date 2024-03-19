import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class BrowserWrapper:
    def __init__(self):
        self.driver = None
        self.json = self.get_json_file()
        self.url_hub = self.json["url_hub"]

    def get_json_file(self):
        with open('C:/Users/rasha\PycharmProjects/terminalxAutomationProject/terminalx.json') as file:
            return json.load(file)


    def get_driver(self, browser_config):
        if browser_config['browserName'] == 'chrome':
            options = ChromeOptions()
        elif browser_config['browserName'] == 'firefox':
            options = FirefoxOptions()
        elif browser_config['browserName'] == 'edge':
            options = EdgeOptions()
        # Add code to initialize the driver based on browser_config
        if self.json.get("grid", False):  # Assuming 'grid' key is a boolean
            return webdriver.Remote(command_executor=self.url_hub, options=options)
        else:
            if browser_config['browserName'] == 'chrome':
                return webdriver.Chrome(options=options)
            elif browser_config['browserName'] == 'firefox':
                return webdriver.Firefox(options=options)
            elif browser_config['browserName'] == 'edge':
                return webdriver.Edge(options=options)


    def get_cap_list(self):
        capabilities = self.json.get("capabilities", [])
        if not capabilities:
            raise ValueError("Missing 'capabilities' configuration in config.json")
        return capabilities

    def get_teardown(self):
        if self.driver:
            self.driver.quit()