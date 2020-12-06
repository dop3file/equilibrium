import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.response = None
        self.all_html = None

    def create_connection(self, link: str) -> None:
        self.response = requests.get(link.replace("'", ''))
        self.all_html = self.response.text

    def read_all_html(self):
        return self.all_html



