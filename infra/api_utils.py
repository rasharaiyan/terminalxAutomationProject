import requests


class APIUtils:
    @staticmethod
    def login(base_url, user_name, password):
        url = base_url + '/pg/MutationUserLogin'

        payload = {"username": user_name,
                   "password": password}

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("POST request was successful!")
        else:
            print("POST request failed with status code:", response.status_code)

        print("Response content:", response.text)
        cookies = response.cookies

        private_content_version_cookie = cookies.get('private_content_version')
        counter_cookie = cookies.get('counter')
        PHPSESSID_cookie = cookies.get('PHPSESSID')
        return response.json(), private_content_version_cookie, counter_cookie, PHPSESSID_cookie

    @staticmethod
    def add_to_cart(base_url, qty, sku, private_content_version_cookie, counter_cookie, PHPSESSID_cookie):
        url = base_url + '/pg/MutationAddAnyProductsToAnyCart'

        headers = {
            'Cookie': 'counter=' + counter_cookie + '; PHPSESSID=' + PHPSESSID_cookie + '; private_content_version=' + private_content_version_cookie
        }

        payload = {"cart_items": [{"data": {"quantity": qty, "any_sku": ""+sku+""}}], "skip_collect": 1}

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            print("POST request was successful!")
        else:
            print("POST request failed with status code:", response.status_code)

        #print("Response content:", response.text)
        return response.json()

    @staticmethod
    def get_current_user_cart_info(base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie):
        url = base_url + '/pg/QueryCurrentUserInfo'

        headers = {
            'Cookie': 'counter=' + counter_cookie + '; PHPSESSID=' + PHPSESSID_cookie + '; private_content_version=' + private_content_version_cookie
        }

        payload = {"withCartObject": True, "withCartItems": True}

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            print("POST request was successful!")
        else:
            print("POST request failed with status code:", response.status_code)

        #print("Response content:", response.text)
        return response.json()

    @staticmethod
    def update_item_in_cart(base_url, qty, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id):
        url = base_url + '/pg/MutationUpdateAnyCartItems'

        headers = {
            'Cookie': 'counter=' + counter_cookie + '; PHPSESSID=' + PHPSESSID_cookie + '; private_content_version=' + private_content_version_cookie
        }

        payload = {"cart_items": [{"cart_item_id": int(item_id), "quantity": qty}], "withMultipass": False,
                   "skip_collect": 1}

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            print("POST request was successful!")
        else:
            print("POST request failed with status code:", response.status_code)

        #print("Response content:", response.text)
        return response.json()

    @staticmethod
    def remove_item_from_cart(base_url, private_content_version_cookie, counter_cookie, PHPSESSID_cookie, item_id):
        url = base_url + '/pg/MutationRemoveItemFromAnyCart'

        headers = {
            'Cookie': 'counter=' + counter_cookie + '; PHPSESSID=' + PHPSESSID_cookie + '; private_content_version=' + private_content_version_cookie
        }

        # Define the payload (data) to be sent in the POST request
        payload = {"cart_item_id": int(item_id), "withMultipass": False, "skip_collect": 1}

        # Send the POST request with the payload
        response = requests.post(url, json=payload, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            print("POST request was successful!")
        else:
            print("POST request failed with status code:", response.status_code)


        # print("Response content:", response.text)
        return response.json()
