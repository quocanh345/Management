from sources.app import app

client = app.test_client()

def test_home():
    res = client.get('/')
    assert res.status_code == 200

