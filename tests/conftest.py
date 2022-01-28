from datetime import datetime
from pathlib import Path
import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixturetest
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config


@pytest.fixture
def browser(config):
    if config['browser'] == 'Firefox':
        brw = webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        brw = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif config['browser'] == 'Headless Chrome':
        opts = Options()
        opts.add_argument('headless')
        brw = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    
    brw.implicitly_wait(config['implicit_wait'])

    yield brw

    brw.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    reports_dir = Path('reports')
    reports_dir.mkdir(parents=True, exist_ok=True)
    report = reports_dir / f"report_{now.strftime('%Y-%m-%d__%H%M%S')}.html"
    config.option.htmlpath = report
    config.option.self_contained_html = True


