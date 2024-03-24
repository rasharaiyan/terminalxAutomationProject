from infra.api_test_base import APITestBase
from logic.api_page import UserPage


class RemoveFromCartThroughAPI(APITestBase):

    def setUp(self):
        self.base_url = self.config['Tests']['baseURL']
        self.email = self.config['Tests']['loginCredentials']['email']
        self.password = self.config['Tests']['loginCredentials']['password']
        self.expected_user_name = self.config['Tests']['loginCredentials']['expected_user_name']
        self.customer_id = self.config['Tests']['customerInfo']['customer_id']
        self.qty = self.config['Tests']['product']['qty']
        self.qty_update = self.config['Tests']['product']['qty_update']

    def test_remove_item_from_cart(self):
        response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(self.base_url, self.email, self.password)
        response = UserPage.get_user_cart_info(self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)
        item_id = response['data']['currentUserInfo']['cart_object']['items'][0]['id']
        response = UserPage.remove_item_from_cart(self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id)
        assert response['data']['removeItemFromAnyCart']['total_quantity'] == 0
