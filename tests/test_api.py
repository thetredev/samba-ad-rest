import time

import pytest


@pytest.mark.order(1)
def test_something():
    time.sleep(6)
    assert True


@pytest.mark.order(2)
def test_something_else():
    time.sleep(7)
    assert True
