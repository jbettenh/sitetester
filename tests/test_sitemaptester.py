from sitemaptester import __version__

import requests


def test_version():
    assert __version__ == '0.1.0'


def test_page():
    url = 'https://www.google.com'

    response = requests.get(url)

    assert response.status_code == 200
