import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        pass

    def create_connection(self, link: str) -> None:
        self.response = requests.get(link)
        self.all_html = self.response.text
        print(self.all_html)




