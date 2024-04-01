import unittest
from api_tests.test_api_add_item_to_cart_functionality import AddToCartThroughAPI
from ui_tests.test_verify_added_product_to_cart import TestVerifyAddedProductToCart
from ui_tests.test_price_sorting import TestPriceSorting
# Initialize test loader
loader = unittest.TestLoader()

test_api_add_to_cart = loader.loadTestsFromTestCase(AddToCartThroughAPI)
test_add_to_cart_test = loader.loadTestsFromTestCase(TestVerifyAddedProductToCart)
test_suite = unittest.TestSuite([test_api_add_to_cart, test_add_to_cart_test])
test_runner = unittest.TextTestRunner()
test_runner.run(test_suite)

test_price_sorting = loader.loadTestsFromTestCase(TestPriceSorting)
test_suite = unittest.TestSuite([test_price_sorting])
test_runner.run(test_suite)