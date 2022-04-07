import requests

API_URL = "http://127.0.0.1:8000"


def test_get_index():
    response = requests.get(
        url=f"{API_URL}/"
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert "hello" in data
    assert data["hello"] == "world"


def test_get_ma_route():
    response = requests.get(
        url=f"{API_URL}/ma_route"
    )
    assert response.status_code == 200, response.content
    data = response.json()

    assert "method" in data
    assert "endpoint" in data

    assert data["method"] == "GET"
    assert data["endpoint"] == "/ma_route"


def test_post_mon_post():
    response = requests.post(
        url=f"{API_URL}/mon_post",
        params={
            "nombre_entier": 42
        }
    )
    assert response.status_code == 200, response.content
    data = response.json()

    assert "nombre_entier" in data
    assert data["nombre_entier"] == 42


def test_get_health():
    response = requests.get(
        url=f"{API_URL}/health"
    )
    assert response.status_code == 200, response.content
    data = response.json()

    assert "status" in data
    assert data["status"] == 1


def test_get_health():
    response = requests.get(
        url=f"{API_URL}/bye"
    )
    assert response.status_code == 200, response.content
    data = response.json()

    assert "bye" in data
    assert data["bye"] == "bye"
