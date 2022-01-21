import pytest
import requests

from sitemaptester import __version__
from pages.homepage import Footer


urls = [
    ('https://www.apple.com/sitemap/', 200),
    ('https://www.raspberrypi.org/', 200)
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

    footer_component = Footer(browser)
    footer_component.load()
    footer_component.get_links()

    assert title == footer_component.title()


def test_html_elements(browser):
    # footer_link = "For educators"
    #
    # footer_component = Footer(browser)
    # footer_component.load()
    #
    # assert footer_link == footer_component.search_for_link()
    pass

def test_json_response():
    pass


