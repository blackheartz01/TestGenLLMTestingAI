from PAapp import Task

import pytest
import math
from fastapi.testclient import TestClient
from PAapp import new_app

client = TestClient(new_app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Banking application!"}

def test_create_user_valid_input():
    task_data = {"name": "Alice", "balance": 100}
    response = client.post("/create_user/", json=task_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
    assert response.json()["balance"] == 100


