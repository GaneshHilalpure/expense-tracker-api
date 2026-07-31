from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200

def test_total_expenses():
    response = client.get("/expenses/total")
    assert response.status_code == 200

def test_add_expense():
    expense = {
        "id": 100,
        "title": "Test Expense",
        "amount": 50,
        "category": "Testing",
        "date": "2026-07-31"
    }

    response = client.post("/expenses", json=expense)
    assert response.status_code == 200

def test_delete_expense():
    response = client.delete("/expenses/100")
    assert response.status_code == 200