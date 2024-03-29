from infra.api_test_base import APITestBase
from logic.api_page import UserPage


class UpdateInCartThroughAPI(APITestBase):

    def setUp(self):
        self.base_url = self.config['Tests']['baseURL']
        self.email = self.config['Tests']['loginCredentials']['email']
        self.password = self.config['Tests']['loginCredentials']['password']
        self.expected_user_name = self.config['Tests']['loginCredentials']['expected_user_name']
        self.customer_id = self.config['Tests']['customerInfo']['customer_id']
        self.qty = self.config['Tests']['product']['qty']
        self.sku = self.config['Tests']['product']['sku']
        self.qty_update = self.config['Tests']['product']['qty_update']

    def test_update_item_in_cart(self):
        response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(self.base_url,
                                                                                                    self.email,
                                                                                                    self.password)
        assert response['data']['userLogin']['customer_id'] == self.customer_id

        response = UserPage.get_user_cart_info(self.base_url, private_content_version_cookie, counter_cookie,
                                               PHPSESSID_cookie)
        # Check if the cart is not empty before attempting to access its first item
        if response['data']['currentUserInfo']['cart_object']['items']:
            item_id = response['data']['currentUserInfo']['cart_object']['items'][0]['id']
            print(item_id)

            # Only attempt to update the cart if it is not empty
            response = UserPage.update_item_in_cart(self.base_url, self.qty_update, private_content_version_cookie,
                                                    counter_cookie, PHPSESSID_cookie, item_id)
            assert response['data']['updateAnyCartItems']['items'][0]['quantity'] == self.qty_update
        else:
            self.fail("The cart is empty. Expected at least one item in the cart.")
