import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.LOGIN_BUTTON = '//div[text()="התחברות"]'
        self.POPUP_LOGIN_BUTTON = '(//div[text()="התחברות"])[1]'
        self.EMAIL_INPUT = '//*[@id="panel-root"]/div/div[3]/div/div/div/div[3]/div[1]/div/form/div[1]/div/input'
        self.PASSWORD_INPUT = '(//input[@name="password"])[1]'
        self.SUBMIT_LOGIN_BUTTON = '//button[@class="tx-link-a submit-btn_2LDW tx-link_29YD btn_1UzJ btn-yellow_2tf3 uppercase_1KUt"]'
        self.USER_NAME_LABEL = '(//button[@class="tx-link-a profile-button_OKk5 profile-button-new-menu_2voE profile-button-icon_1X_h tx-link_29YD"]/span)[2]'

    def navigate_to_site(self, url):
        self.driver.get(url)

    def click_login_button(self):
        # Click on the login button
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def enter_email(self, email):
        # Enter the email
        email_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT))
        )
        email_field.click()
        email_field.send_keys(email)


    def enter_password(self, password):
        # Click on the password input field and enter the password
        password_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.PASSWORD_INPUT))
        )
        password_field.click()
        password_field.send_keys(password)

    def click_submit_login_button(self):
        # Click the submit button
        self.driver.find_element(By.XPATH, self.SUBMIT_LOGIN_BUTTON).click()

    def get_user_name_label_text(self):
        # Get the text of the user name label
        return self.driver.find_element(By.XPATH, self.USER_NAME_LABEL).text
