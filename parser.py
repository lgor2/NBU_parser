import requests


def parse():
    response = requests.get('https://coins.bank.gov.ua/catalog.html?page=1&sort=catalog')
    page = response.text
    print(page)


parse()
