import json

import pytest

from .base_client import BaseClient


class TodoClient(BaseClient):
    def __init__(self, client):
        super().__init__(client, endpoint_path="todo")


@pytest.fixture
def todo_client(client):
    return TodoClient(client)


@pytest.fixture
def todo(make_todo):
    return make_todo()


def test_create_todo(session, todo_client):
    data = {
        "description": "string",
    }
    response = todo_client.create(json.dumps(data))

    assert response.status_code == 200
    assert response.json()["description"] == "string"
