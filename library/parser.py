"""
Файл библиотеки Parser
"""
import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.response = None
        self.all_html = None
        self.parser = None

    def create_connection(self, link: str) -> None:
        self.response = requests.get(link.replace("'", ''))
        self.all_html = self.response.text
        self.parser = BeautifulSoup(self.all_html, 'html.parser')

    def title_page(self):
        return f'"""{self.parser.title}"""'

    def get_all_html(self):
        return f'"""{self.all_html}"""'







