from fastapi.testclient import TestClient
from .online_model import app, model


def test_predict():
    with TestClient(app) as client:
        response = client.get(
            "/predict/",
            json={"data": [[69, 1, 0, 160, 234, 1, 2, 131, 0, 0.1, 1, 1, 0],
                         [69, 0, 0, 140, 239, 0, 0, 151, 0, 1.8, 0, 2, 0],
                         [66, 0, 0, 150, 226, 0, 0, 114, 0, 2.6, 2, 0, 0]],
                "features": [
                    "age", "sex", "cp", "trestbps",
                    "chol", "fbs", "restecg", "thalach",
                    "exang", "oldpeak", "slope", "ca", "thal"]
            }
        )
        assert response.status_code == 200
        assert response.json() == [{"condition": 0},
                                   {"condition": 0},
                                   {"condition": 0}
                                   ]
