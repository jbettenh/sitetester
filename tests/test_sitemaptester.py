from sitemaptester import __version__
import pytest
import requests

urls = [
    ('https://www.google.com', 200),
    ('https://www.google.de', 200),
    ('https://www.google.ch', 200),
    ('https://www.google.at', 200),
    ('https://www.google.uk', 200)
]


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize('url, expected_code', urls)
def test_page_exists(url, expected_code):
    """ Check all pages are available """
    response = requests.get(url)

    assert response.status_code == expected_code
