from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test 1: Normal subtraction
def test_subtraction():
    response = client.get("/subtract?num1=20&num2=10")

    assert response.status_code == 200
    assert response.json()["result"] == 10


# Test 2: Negative result
def test_negative_result():
    response = client.get("/subtract?num1=5&num2=10")

    assert response.status_code == 200
    assert response.json()["result"] == -5


# Test 3: Decimal subtraction
def test_decimal_result():
    response = client.get("/subtract?num1=10.5&num2=2.5")

    assert response.status_code == 200
    assert response.json()["result"] == 8