from datetime import datetime
from pathlib import Path
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    reports_dir = Path('reports')
    reports_dir.mkdir(parents=True, exist_ok=True)
    report = reports_dir / f"report_{now.strftime('%Y-%m-%d__%H%M%S')}.html"
    config.option.htmlpath = report
    config.option.self_contained_html = True


