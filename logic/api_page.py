from infra.api_utils import APIUtils


class UserPage:
    @staticmethod
    def login(base_url, user_name, password):
        return APIUtils.login(base_url, user_name, password)

    @staticmethod
    def add_to_cart(base_url, qty, sku, private_content_version_cookie, counter_cookie, PHPSESSID_cookie):
        return APIUtils.add_to_cart(base_url, qty, sku, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)

    @staticmethod
    def get_user_cart_info(base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie):
        return APIUtils.get_current_user_cart_info(base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie)

    @staticmethod
    def update_item_in_cart(base_url, qty, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id):
        return APIUtils.update_item_in_cart(base_url, qty, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id)

    @staticmethod
    def remove_item_from_cart(base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id):
        return APIUtils.remove_item_from_cart(base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id)