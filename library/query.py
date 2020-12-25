import requests


class Query:
    def __init__(self):
        pass

    def get_request(self, link):
        requests.get(link)

    def post_request(self, link):
        requests.post(link)
