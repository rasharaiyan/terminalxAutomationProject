import unittest
from tests.api_tests.test_api_add_item_to_cart_functionality import AddToCartThroughAPI
from tests.api_tests.test_api_remove_item_from_cart_functionality import RemoveFromCartThroughAPI
from tests.api_tests.test_api_update_item_in_cart_functionality import UpdateInCartThroughAPI
from tests.ui_tests.test_verify_added_product_to_cart import TestVerifyAddedProductToCart
from tests.ui_tests.test_verify_updated_product_qty_in_cart import TestVerifyUpdatedProductQtyInCart
from tests.ui_tests.test_verify_deleted_product_from_cart import TestVerifyDeletedProductFromCart

# Initialize test loader
loader = unittest.TestLoader()

api_add_to_cart = loader.loadTestsFromTestCase(AddToCartThroughAPI)
add_to_cart_test = loader.loadTestsFromTestCase(TestVerifyAddedProductToCart)
test_suite = unittest.TestSuite([api_add_to_cart])
test_runner = unittest.TextTestRunner()
test_runner.run(test_suite)

api_update_in_cart = loader.loadTestsFromTestCase(UpdateInCartThroughAPI)
update_qty_in_cart_test = loader.loadTestsFromTestCase(TestVerifyUpdatedProductQtyInCart)
test_suite = unittest.TestSuite([api_update_in_cart])
test_runner = unittest.TextTestRunner()
test_runner.run(test_suite)

api_remove_from_cart = loader.loadTestsFromTestCase(RemoveFromCartThroughAPI)
delete_product_from_cart_test = loader.loadTestsFromTestCase(TestVerifyDeletedProductFromCart)
test_suite = unittest.TestSuite([api_remove_from_cart])
test_runner = unittest.TextTestRunner()
test_runner.run(test_suite)