import unittest
from tests.ui_tests.test_add_item_to_cart import TestAddToCartFunctionality
from tests.ui_tests.test_wishlist_functionality import TestWishlistFunctionality
from tests.ui_tests.test_update_item_quantity import TestUpdateCartFunctionality
from tests.ui_tests.test_usability_responsive_design import TestResponsiveDesign
from tests.ui_tests.test_color_accessibility import TestColorAccessibility
from tests.ui_tests.test_search_functionallity import SearchFunctionality
from tests.ui_tests.test_price_sorting import TestPriceSorting
from tests.ui_tests.test_follow_us_navigation import TestFollowUsNavigation

# Initialize test loader
loader = unittest.TestLoader()

# Load test cases
add_to_cart_test = loader.loadTestsFromTestCase(TestAddToCartFunctionality)
wishlist_test = loader.loadTestsFromTestCase(TestWishlistFunctionality)
update_quantity_test = loader.loadTestsFromTestCase(TestUpdateCartFunctionality)
usability_test=loader.loadTestsFromTestCase(TestResponsiveDesign)
accessibility_test=loader.loadTestsFromTestCase(TestColorAccessibility)
search_functionality_test=loader.loadTestsFromTestCase(SearchFunctionality)
price_sorting_test=loader.loadTestsFromTestCase(TestPriceSorting)
follow_us_test=loader.loadTestsFromTestCase((TestFollowUsNavigation))

# Create test suite
test_suite = unittest.TestSuite([add_to_cart_test, wishlist_test, update_quantity_test,usability_test,
                                 accessibility_test,search_functionality_test,price_sorting_test,follow_us_test])

# Initialize test runner
test_runner = unittest.TextTestRunner()

# Run the test suite
test_runner.run(test_suite)
