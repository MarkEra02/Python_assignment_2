import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        pass

    def get(self, currency):
        page = requests.get(
            "https://google.com/search?q=site%3Acoinmarketcap.com+" + currency + "&ie=utf-8&oe=utf-8")
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find_all("h3")
        return result

cryptocurrency_name = input()

scrapper = Scrapper()
list = scrapper.get(cryptocurrency_name)

for el in list:
    print(el.find("div").get_text())