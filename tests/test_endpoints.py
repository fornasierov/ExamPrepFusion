import os, sys
from fastapi.testclient import TestClient

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.main import app

client = TestClient(app)


def test_summarize():
    """
    Test if the summarize returns a JSON containing the summary.
    """
    response = client.post(
        "/summarize/", json={"guidelines": ["Fast for 8 hours.", "Study well."]}
    )
    assert response.status_code == 200
    assert "summary" in response.json()
