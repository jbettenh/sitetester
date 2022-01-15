class Footer:
    URL = 'https://www.raspberrypi.org/'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self):
        return self.browser.title

    def search_for_link(self):
        pass