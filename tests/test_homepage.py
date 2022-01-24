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
    assert len(urls) == 26


def test_footer_links(browser):
    expected_links = {'For educators': 'https://www.raspberrypi.org/teach',
                      'Teach Computing': 'https://teachcomputing.org/',
                      'Isaac Computer Science': 'https://isaaccomputerscience.org/',
                      'Research': 'https://www.raspberrypi.org/research',
                      'Hello World magazine': 'https://helloworld.raspberrypi.org/',
                      'For learners': 'https://www.raspberrypi.org/learn',
                      'CoderDojo': 'https://coderdojo.com/', 'Code Club': 'https://codeclub.org/',
                      'Code Club World': 'https://codeclubworld.org/',
                      'Explore our projects': 'https://projects.raspberrypi.org',
                      'Astro Pi': 'https://astro-pi.org/', 'Coolest Projects': 'https://online.coolestprojects.org/',
                      'Safeguarding': 'https://www.raspberrypi.org/safeguarding',
                      'Accessibility': 'https://www.raspberrypi.org/accessibility',
                      'Privacy': 'https://www.raspberrypi.org/privacy',
                      'Cookies': 'https://www.raspberrypi.org/cookies',
                      'About us': 'https://www.raspberrypi.org/about',
                      'Donate': 'https://www.raspberrypi.org/donate',
                      'Team': 'https://www.raspberrypi.org/about/meet-the-team',
                      'Careers': 'https://raspberrypifoundation.workable.com',
                      'Governance': 'https://www.raspberrypi.org/about/governance',
                      'Contact us': 'https://www.raspberrypi.org/contact',
                      'Trademark & brand': 'https://www.raspberrypi.org/trademark-rules',
                      'Raspberry Pi computers': 'https://www.raspberrypi.com'}

    page = PageBody(browser)

    page.load()
    actual_links = page.get_links('c-footer__nav-link')

    assert len(actual_links) > 0
    assert actual_links == expected_links


