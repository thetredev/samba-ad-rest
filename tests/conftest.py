import time
from multiprocessing import Process
from pathlib import Path

import pytest

from ad.entry import main as ad_main


@pytest.fixture
def api_server():
    # start the server before a test is run
    api_process = Process(target=ad_main, args=[Path("configs/test.toml")])
    api_process.start()
    yield

    # terminate the server after a test has run
    api_process.terminate()

    # ... and wait for it to exit
    while api_process.is_alive():
        time.sleep(0.1)


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(session: pytest.Session, config: pytest.Config, items: list[pytest.Item]):
    # add all fixtures to all tests after test collection
    for item in items:
        item.fixturenames.append(api_server.__name__)
