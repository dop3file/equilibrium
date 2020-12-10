"""
Файл библиотеки Parser
"""
import requests
from bs4 import BeautifulSoup
from lxml import html


class Parser:
    def __init__(self):
        self.response = None
        self.all_html = None
        self.parser = None
        self.link = None

    def create_connection(self, link: str) -> None:
        """
        Инициализация класса Parser
        :param link: ссылка на сайт
        :return: None
        """
        self.link = link.replace("'", '')
        self.response = requests.get(link.replace("'", ''))
        self.all_html = self.response.text
        self.parser = BeautifulSoup(self.all_html, 'html.parser')

    def title_page(self):
        """
        :return: возвращает заголовок сайта
        """
        return self.parser.title.string

    def get_xpath(self, xpath):
        """
        :param xpath: путь к элементу в DOM дереве
        :return: функция возвращает текст элемента
        """
        page = requests.get(self.link)
        tree = html.fromstring(page.content)

        return tree.xpath(xpath.replace("'", ''))[0]

    def get_link(self):
        """
        :return: функция возвращает ссылку на сайт, инициализированный в классе
        """
        return f"'{self.link}'"







