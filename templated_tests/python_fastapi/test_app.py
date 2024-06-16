import pytest
import math
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    """
    Test the root endpoint by sending a GET request to "/" and checking the response status code and JSON body.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Banking application!"}

def test_sqrt_positive_input():
    response = client.get("/sqrt/16")
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}


def test_multiply_with_zero():
    response = client.get("/multiply/10/0")
    assert response.status_code == 200
    assert response.json() == {"result": 0}


def test_subtract_positive_integers():
    response = client.get("/subtract/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_days_until_new_year():
    response = client.get("/days-until-new-year")
    assert response.status_code == 200
    assert "days_until_new_year" in response.json()


def test_is_palindrome_palindrome():
    response = client.get("/is-palindrome/radar")
    assert response.status_code == 200
    assert response.json() == {"is_palindrome": True}


def test_divide_by_zero():
    response = client.get("/divide/10/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}


def test_square_positive_integer():
    response = client.get("/square/4")
    assert response.status_code == 200
    assert response.json() == {"result": 16}


def test_divide_valid_inputs():
    response = client.get("/divide/10/2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_add_positive_integers():
    response = client.get("/add/5/3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_current_date():
    response = client.get("/current-date")
    assert response.status_code == 200
    assert "date" in response.json()

