from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver import ActionChains

class FollowUs(BasePage):
    # XPaths for elements for follow us page
    FOLLOW_US_PAGE_XPATH = '//div[@class="socialWrapper_3GFm"]'
    INSTAGRAM_ICON_XPATH = '//a[@href="https://www.instagram.com/terminalx"]'
    FACEBOOK_ICON_XPATH='//a[@href="https://www.facebook.com/WEARETERMINALX/"]'
    YOUTUBE_ICON_XPATH= '//a[@href="https://www.youtube.com/channel/UCUTXP6iS-VyE1Vxllg_3W5g?view_as=subscriber"]'

    def navigate_to_follow_us(self):
            follow_us_element = self._driver.find_element(By.XPATH, self.FOLLOW_US_PAGE_XPATH)
            actions = ActionChains(self._driver)
            actions.move_to_element(follow_us_element).perform()

    def click_instagram_icon(self): #Clicks the Instagram icon on the Join Us page.
        self._driver.find_element(By.XPATH, self.INSTAGRAM_ICON_XPATH).click()

    def click_facebook_icon(self): #Clicks the Facebook icon on the Join Us page.
        self._driver.find_element(By.XPATH, self.FACEBOOK_ICON_XPATH).click()

    def click_youtube_icon(self): #Clicks the LinkedIn icon on the Join Us page.
        self._driver.find_element(By.XPATH, self.YOUTUBE_ICON_XPATH).click()