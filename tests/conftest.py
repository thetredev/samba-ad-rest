import socket
import time
from multiprocessing import Process
from pathlib import Path

import pytest

from samba_ad_rest_api.config import ServerConnection, read_config
from samba_ad_rest_api.entry import main as ad_main


@pytest.fixture
def server_connection():
    config_path = Path("configs/test.toml")

    # start the server before a test is run
    api_process = Process(
        target=ad_main, args=[
            config_path
        ]
    )

    api_process.start()

    # read the config data the process has been started with
    config_data = read_config(config_path)
    config_host = config_data.server.host
    config_port = config_data.server.port

    # wait for the server to be ready (config_data.port is open)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_stream:
        while socket_stream.connect_ex((config_host, config_port)) != 0:
            time.sleep(0.1)

    # yield the config data
    # => run the test
    yield ServerConnection(config_host, config_port)

    # terminate the server after test has run
    api_process.terminate()

    # ... and wait for it to exit
    api_process.join()


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(items: list[pytest.Item]):
    fixtures = [
        server_connection.__name__
    ]

    # add all fixtures to all tests after test collection
    for item in items:
        item.fixturenames.extend(fixtures)
