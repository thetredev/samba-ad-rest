import pytest
from samba_ad_rest_api.config import ServerConnection


@pytest.mark.order(1)
def test_something(server_connection: ServerConnection):
    print(server_connection)
    assert True


@pytest.mark.order(2)
def test_something_else(server_connection: ServerConnection):
    print(server_connection)
    assert True
