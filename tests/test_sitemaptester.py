from sitemaptester import __version__
import pytest
import requests

urls = [
    ('https://www.apple.com/sitemap/', 200)
]


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize('url, expected_code', urls)
def test_page_exists(url, expected_code):
    """ Check all pages are available """
    response = requests.get(url)

    assert response.status_code == expected_code


def test_response_time():
    pass


def test_number_of_pages():
    pass


def test_html_headers():
    pass


def test_html_elements():
    pass


def test_json_response():
    pass


