import requests
from bs4 import BeautifulSoup


def get_page(href):
    response = requests.get(href)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')

    return soup


def parse(href):
    set_of_items = set()
    link_to_next_page = href
    number_of_page = 1
    next_page_exists = True

    while next_page_exists:
        soup = get_page(link_to_next_page)
        items = soup.findAll('div', class_='p_description')

        for i in items:
            name = i.find('a', class_='model_product').text
            price = i.find('span', class_='new_price').text

            set_of_items.add((name, price))

        next_page_exists = bool(soup.find('a', class_='next_page'))

        number_of_page += 1

        if next_page_exists:
            link_to_next_page = f'https://coins.bank.gov.ua/catalog.html?page={number_of_page}&sort=catalog'

    return set_of_items
#
#
# sss = parse('https://coins.bank.gov.ua/catalog.html?page=2&sort=catalog')
#
# for i in sss:
#     print(i)
#
# print(len(list(sss)))
