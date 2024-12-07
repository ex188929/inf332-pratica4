from vagago_api.main import create_app
import pytest


@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_say_hello(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}
