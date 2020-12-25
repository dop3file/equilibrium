"""
Файл библиотеки Parser для парсинга информации с вебсайтов
"""
import requests
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
        try:
            tree = html.fromstring(self.all_html)
            return f"'{tree.xpath(xpath)[0].text_content()}'"
        except Exception:
            pass

    def get_link(self):
        """
        :return: функция возвращает ссылку на сайт, инициализированный в классе
        """
        return f"'{self.link}'"
