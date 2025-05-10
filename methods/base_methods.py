import requests

class BaseMethods:

    @staticmethod
    def post_request(url, payload):
        return requests.post(url, json=payload)

    @staticmethod
    def get_request(url):
        return requests.get(url)

    @staticmethod
    def delete_request(url):
        return requests.delete(url)


    @staticmethod
    def patch_request(url):
        return requests.patch(url)