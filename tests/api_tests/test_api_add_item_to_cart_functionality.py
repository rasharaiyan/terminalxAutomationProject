from infra.api_test_base import APITestBase
from logic.api_page import UserPage


class AddToCartThroughAPI(APITestBase):

    def setUp(self):
        self.base_url = self.config['Tests']['baseURL']
        self.email = self.config['Tests']['loginCredentials']['email']
        self.password = self.config['Tests']['loginCredentials']['password']
        self.expected_user_name = self.config['Tests']['loginCredentials']['expected_user_name']
        self.customer_id = self.config['Tests']['customerInfo']['customer_id']
        self.qty = self.config['Tests']['product']['qty']
        self.sku = self.config['Tests']['product']['sku']
        self.qty_update = self.config['Tests']['product']['qty_update']

    def clear_cart(self):
        # Log in to get the necessary cookies and session information
        response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(self.base_url,
                                                                                                    self.email,
                                                                                                    self.password)
        assert response['data']['userLogin']['customer_id'] == self.customer_id

        # Get current cart info
        response = UserPage.get_user_cart_info(self.base_url, private_content_version_cookie, counter_cookie,
                                               PHPSESSID_cookie)
        items = response['data']['currentUserInfo']['cart_object']['items']

        # Remove all items from the cart
        for item in items:
            item_id = item['id']
            response = UserPage.remove_item_from_cart(self.base_url, private_content_version_cookie, counter_cookie,
                                                      PHPSESSID_cookie, item_id)
            assert response['data']['removeItemFromAnyCart'][
                       'total_quantity'] >= 0  # Check this condition based on how your API behaves
    def test_add_item_to_cart(self):
        self.clear_cart()
        response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(self.base_url, self.email,  self.password)

        assert response['data']['userLogin']['customer_id'] == self.customer_id

        response = UserPage.add_to_cart(self.base_url, self.qty, self.sku, private_content_version_cookie,
                                        counter_cookie, PHPSESSID_cookie)
        assert response['data']['addAnyProductsToAnyCart']['total_quantity'] == self.qty
