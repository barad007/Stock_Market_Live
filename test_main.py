from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/stockPrices/getAll/aap")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def test_stock_prices_invalid_route():
    response = client.get("/stockPrices/get")
    assert response.status_code == 404
    assert response.headers["content-type"] == "application/json"

def test_stock_prices_in_range():
    response = client.get("/stockPrices/GOOGL/interval/1d/period/1mo")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def test_stock_prices_in_range_invalid_interval():
    response = client.get("/stockPrices/GOOGL/interval/15s/period/1mo")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def test_stock_prices_in_range_invalid_period():
    response = client.get("/stockPrices/GOOGL/interval/1d/period/3y")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"