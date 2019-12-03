import pytest

from funbox import create_app
from funbox.db import get_connection


@pytest.fixture
def app():
    app = create_app(testing=True)
    with get_connection(app.config['DATABASE']) as r:
        r.flushall()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
