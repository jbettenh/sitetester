from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By


class PageBody:
    URL = 'https://www.raspberrypi.org/'

    SEARCH_INPUT = (By.ID, 'search_link')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self):
        return self.browser.title

    def search_for_link(self):
        search_input = self.browser.find_element("For educators").text
        return search_input


