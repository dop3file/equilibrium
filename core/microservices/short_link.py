import requests


class ShortLink:
    @staticmethod
    def add_link(value):
        true_url = value.split(' ')[0].replace("'",'')
        redirect_url = value.split(' ')[1].replace("'",'')

        print(requests.post(url='http://equilibriumshortlink.pythonanywhere.com/create_link',params={'link': true_url,'redirect_link': redirect_url}).json())