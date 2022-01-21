from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.raspberrypi.org'


def get_links(search_class):
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = {}

    for link in soup.find_all('a', class_=search_class):
        links[link.text] = link['href']

    return links


def create_abs_links(relative_links):
    abs_links = relative_links

    for text, link in abs_links.items():
        if 'http' not in link:
            abs_links[text] = BASE_URL + link

    return abs_links


if __name__ == '__main__':
    test = get_links('c-footer__nav-link')
    test2 = create_abs_links(test)
    print(f'links found {test2}')