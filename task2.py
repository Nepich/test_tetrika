import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE' \
      '%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83 '
all_animals = set()
ua = UserAgent().random


def get_animals_from_page(path):
    """Функция парсинга животных во множество животных"""
    data = requests.get(url=path, headers={'user-agen': ua})
    soap = BeautifulSoup(data.content, 'lxml')
    for animal in soap.find('div', attrs={'class': 'mw-category mw-category-columns'}).find_all('a'):
        if ord(animal.text[0].lower()) in range(ord('а'), (ord('я') + 1)):
            all_animals.add(animal.text)


def get_next_urls(path):
    """Функция получения следующей страницы вики с русскими названиями животных"""
    data = requests.get(url=path, headers={'user-agen': ua})
    soap = BeautifulSoup(data.content, 'lxml')
    for href in soap.find('div', attrs={'id': 'mw-pages'}).\
            find_all('a', attrs={'title': 'Категория:Животные по алфавиту'}, recursive=False):
        if href.text == 'Следующая страница':
            next_page = 'https://ru.wikipedia.org' + href.get('href')
            return next_page


if __name__ == '__main__':
    while not ('Ящурки' in all_animals):
        get_animals_from_page(url)
        url = get_next_urls(url)
    dct = {}
    for i in range(ord('А'), (ord('Я')+1)):
        dct[chr(i)] = len(list(filter(lambda x: x if x[0] == chr(i) else None, all_animals)))
    for key, value in dct.items():
        print(f'{key}: {value}')
