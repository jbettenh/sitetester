import pytest
import requests

from sitemaptester import __version__
from pages.homepage import PageBody


urls = [
    ('https://www.raspberrypi.org/', 200),
    ('https://www.raspberrypi.org/teach', 200),
    ('https://teachcomputing.org/', 200),
    ('https://isaaccomputerscience.org/', 200),
    ('https://isaaccomputerscience.org/', 200),
    ('https://www.raspberrypi.org/research', 200),
    ('https://helloworld.raspberrypi.org/', 200),
    ('https://www.raspberrypi.org/learn', 200),
    ('https://coderdojo.com/', 200),
    ('https://codeclub.org/', 200),
    ('https://codeclubworld.org/', 200),
    ('https://projects.raspberrypi.org', 200),
    ('https://astro-pi.org/', 200),
    ('https://online.coolestprojects.org/', 200),
    ('https://www.raspberrypi.org/safeguarding', 200),
    ('https://www.raspberrypi.org/accessibility', 200),
    ('https://www.raspberrypi.org/privacy', 200),
    ('https://www.raspberrypi.org/cookies', 200),
    ('https://www.raspberrypi.org/about', 200),
    ('https://www.raspberrypi.org/donate', 200),
    ('https://www.raspberrypi.org/about/meet-the-team', 200),
    ('https://raspberrypifoundation.workable.com', 200),
    ('https://www.raspberrypi.org/about/governance', 200),
    ('https://www.raspberrypi.org/contact', 200),
    ('https://www.raspberrypi.org/trademark-rules', 200),
    ('https://www.raspberrypi.com', 200),
]


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize('url, expected_code', urls)
def test_page_exists(url, expected_code):
    """ Check all pages are available """
    response = requests.get(url)

    assert response.status_code == expected_code


def test_response_time():
    response = requests.get('https://www.raspberrypi.org/')

    assert response.elapsed.total_seconds() < 1.00


def test_number_of_pages():
    pass


def test_html_headers(browser):
    title = 'Teach, Learn, and Make with Raspberry Pi'
    phrase = 'https://teachcomputing.org/'
    page = PageBody(browser)
    page.load()

    titles = page.get_links('c-footer__nav-link')
    print(titles)
    assert len(titles) > 0
    assert title == page.title()


def test_html_elements(browser):
    pass


def test_json_response():
    pass


