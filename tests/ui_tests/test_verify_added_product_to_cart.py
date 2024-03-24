import time
import unittest
from selenium import webdriver
from logic.login_functionality import Login
from logic.home_page import HomePage
from infra.test_base import TestBase


class TestVerifyAddedProductToCart(TestBase):

    def setUp(self):
        super().setUp()
        self.base_url = self.config['Tests']['baseURL']
        self.login_page = Login(self.driver)
        self.home_page = HomePage(self.driver)
        self.email = self.config['Tests']['loginCredentials']['email']
        self.password = self.config['Tests']['loginCredentials']['password']
        self.item_sku=self.config['Tests']['product']['sku']
        self.expected_user_name = self.config['Tests']['loginCredentials']['expected_user_name']


    def test_cart_count(self):
        # Navigate to the website
        self.login_page.navigate_to_site(self.base_url)

        # Click on the login button
        self.login_page.click_login_button()

        # Enter the email
        self.login_page.enter_email(self.email)

        # Enter the password
        self.login_page.enter_password(self.password)

        # Click the submit button
        self.login_page.click_submit_login_button()
        time.sleep(3)
        user_name_label_text = self.login_page.get_user_name_label_text()
        time.sleep(3)

        self.assertEqual(str(1), self.home_page.cart_icon(), "Cart count not matched")
