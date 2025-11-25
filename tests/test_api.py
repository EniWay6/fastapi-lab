def test_root(client):
    response = client.get("/")
    assert response.status_code == 200


def test_404(client):
    response = client.get("/shos-ne-isnue")
    assert response.status_code == 404
