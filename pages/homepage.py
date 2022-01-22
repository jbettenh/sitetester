from bs4 import BeautifulSoup


class PageBody:
    URL = 'https://www.raspberrypi.org'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self):
        return self.browser.title

    def get_links(self, search_class):
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        links = {}

        for link in soup.find_all('a', class_=search_class):
            links[link.text] = link['href']

        found_links = self.create_abs_links(links)
        return found_links

    def create_abs_links(self, relative_links):
        abs_links = relative_links

        for text, link in abs_links.items():
            if 'http' not in link:
                abs_links[text] = self.URL + link

        return abs_links
