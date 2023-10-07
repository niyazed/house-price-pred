from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_read_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_read_predict():
    json_input = {
        "features": {
            "avg_area_income": 79545.45857431678,
            "avg_area_house_age": 5.682861321615587,
            "avg_area_number_of_rooms": 7.009188142792237,
            "avg_area_number_of_bedrooms": 4.09,
            "area_population": 23086.800502686456,
            "address": "208 Michael Ferry Apt. 674 Laurabury, NE37010-5101",
        },
        "provider": "payment-api",
    }

    json_output = {
        "features": {
            "avg_area_income": 79545.45857431678,
            "avg_area_house_age": 5.682861321615587,
            "avg_area_number_of_rooms": 7.009188142792237,
            "avg_area_number_of_bedrooms": 4.09,
            "area_population": 23086.800502686456,
            "address": "208 Michael Ferry Apt. 674 Laurabury, NE37010-5101",
        },
        "output": 1244892.75,
        "provider": "payment-api",
    }
    response = client.post("/predict", json=json_input)
    assert response.status_code == 200
    print(response.json())
    assert response.json() == json_output
