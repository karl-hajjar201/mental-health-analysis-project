from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_mental_insights():
    response = client.get("/mental-insights")
    assert response.status_code == 200
    data = response.json()
    assert "top_stress_features" in data
    assert "correlations" in data
    assert isinstance(data["top_stress_features"], list)
    assert isinstance(data["correlations"], dict)


def test_get_daily_insight_success():
    response = client.get("/daily-insight", params={"date": "2024-05-01"})
    assert response.status_code == 200
    data = response.json()
    assert "date" in data
    assert "avg_stress" in data
    assert "notes" in data


def test_get_daily_insight_not_found():
    # Testing with a date with no data should 404
    response = client.get("/daily-insight", params={"date": "1401-01-01"})
    assert response.status_code == 404
    data = response.json()
    assert data["detail"].startswith("No insights found")
