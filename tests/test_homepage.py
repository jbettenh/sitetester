import pytest
import requests

from sitemaptester import __version__
from pages.homepage import PageBody


urls = [
    ('https://www.raspberrypi.org/', 200, 1),
    ('https://www.raspberrypi.org/teach', 200, 1),
    ('https://teachcomputing.org/', 200, 1),
    ('https://isaaccomputerscience.org/', 200, 1),
    ('https://isaaccomputerscience.org/', 200, 1),
    ('https://www.raspberrypi.org/research', 200, 1),
    ('https://helloworld.raspberrypi.org/', 200, 1),
    ('https://www.raspberrypi.org/learn', 200, 1),
    ('https://coderdojo.com/', 200, 1),
    ('https://codeclub.org/', 200, 1),
    ('https://codeclubworld.org/', 200, 1),
    ('https://projects.raspberrypi.org', 200, 1),
    ('https://astro-pi.org/', 200, 1),
    ('https://online.coolestprojects.org/', 200, 1),
    ('https://www.raspberrypi.org/safeguarding', 200, 1),
    ('https://www.raspberrypi.org/accessibility', 200, 1),
    ('https://www.raspberrypi.org/privacy', 200, 1),
    ('https://www.raspberrypi.org/cookies', 200, 1),
    ('https://www.raspberrypi.org/about', 200, 1),
    ('https://www.raspberrypi.org/donate', 200, 1),
    ('https://www.raspberrypi.org/about/meet-the-team', 200, 1),
    ('https://raspberrypifoundation.workable.com', 200, 1),
    ('https://www.raspberrypi.org/about/governance', 200, 1),
    ('https://www.raspberrypi.org/contact', 200, 1),
    ('https://www.raspberrypi.org/trademark-rules', 200, 1),
    ('https://www.raspberrypi.com', 200, 1),
]

footer_links = [
    ('https://www.raspberrypi.org/'),
    ('https://www.raspberrypi.org/teach'),
    ('https://teachcomputing.org/'),
    ('https://isaaccomputerscience.org/'),
    ('https://isaaccomputerscience.org/'),
    ('https://www.raspberrypi.org/research'),
    ('https://helloworld.raspberrypi.org/'),
    ('https://www.raspberrypi.org/learn'),
    ('https://coderdojo.com/'),
    ('https://codeclub.org/'),
    ('https://codeclubworld.org/'),
    ('https://projects.raspberrypi.org'),
    ('https://astro-pi.org/'),
    ('https://online.coolestprojects.org/'),
    ('https://www.raspberrypi.org/safeguarding'),
    ('https://www.raspberrypi.org/accessibility'),
    ('https://www.raspberrypi.org/privacy'),
    ('https://www.raspberrypi.org/cookies'),
    ('https://www.raspberrypi.org/about'),
    ('https://www.raspberrypi.org/donate'),
    ('https://www.raspberrypi.org/about/meet-the-team'),
    ('https://raspberrypifoundation.workable.com'),
    ('https://www.raspberrypi.org/about/governance'),
    ('https://www.raspberrypi.org/contact'),
    ('https://www.raspberrypi.org/trademark-rules'),
    ('https://www.raspberrypi.com'),
]


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize('url, expected_code, elapsed', urls)
def test_page_exists(url, expected_code, elapsed):
    """ Check all pages are available """
    response = requests.get(url)

    assert response.status_code == expected_code


@pytest.mark.parametrize('url, expected_code, elapsed', urls)
def test_response_time(url, expected_code, elapsed):
    response = requests.get(url)

    assert response.elapsed.total_seconds() < elapsed


def test_html_headers(browser):
    title = 'Teach, Learn, and Make with Raspberry Pi'

    page = PageBody(browser)
    page.load()

    assert title == page.title()


def test_number_of_pages():
    assert len(footer_links) == 26


def test_footer_links(browser):
    phrase = 'https://www.raspberrypi.org/about'
    page = PageBody(browser)

    page.load()
    links = page.get_links('c-footer__nav-link')

    assert len(links) > 0
    assert phrase in links.values()


def test_json_response():
    pass


