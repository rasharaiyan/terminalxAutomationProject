from infra.api_test_base import APITestBase
from logic.api_page import UserPage

class RemoveFromCartThroughAPI(APITestBase):

    def setUp(self):
        super().setUp()
        self.test_passed = True  # Initialize test_passed flag as True
        self.base_url = self.config['Tests']['baseURL']
        self.email = self.config['Tests']['loginCredentials']['email']
        self.password = self.config['Tests']['loginCredentials']['password']
        self.expected_user_name = self.config['Tests']['loginCredentials']['expected_user_name']
        self.customer_id = self.config['Tests']['customerInfo']['customer_id']
        self.qty = self.config['Tests']['product']['qty']
        self.sku = self.config['Tests']['product']['sku']
        self.qty_update = self.config['Tests']['product']['qty_update']

    def test_remove_item_from_cart(self):
        try:
            # Log in to get the necessary cookies and session information
            response, private_content_version_cookie, counter_cookie, PHPSESSID_cookie = UserPage.login(
                self.base_url, self.email, self.password)

            # Assert user login is successful
            assert response['data']['userLogin']['customer_id'] == self.customer_id

            # Get current cart info
            response = UserPage.get_user_cart_info(
                self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)

            # Ensure there is at least one item in the cart
            assert response['data']['currentUserInfo']['cart_object']['items'][0]['id'] is not None

            # Extract item ID
            item_id = response['data']['currentUserInfo']['cart_object']['items'][0]['id']

            # Remove item from cart
            response = UserPage.remove_item_from_cart(
                self.base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id)

            # Assert the total quantity in the cart is now 0
            assert response['data']['removeItemFromAnyCart']['total_quantity'] == 0
        except AssertionError:
            # Assertion failed, set test_passed flag to False
            self.test_passed = False
            # Re-raise the exception to mark the test as failed
            raise
        else:
            # All assertions passed, set test_passed flag to True
            self.test_passed = True

    def tearDown(self):
        super().tearDown()  # Call the tearDown method of the parent class
        if not self.test_passed:
            # Assertion failed, create Jira issue using the method from TestBase
            self.report_jira_issue("Update item in Cart Through API Test Assertion Failure",
                                   "Test failed due to assertion failure")
