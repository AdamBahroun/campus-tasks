from app.app import app

def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 404


def test_echec_volontaire():
    assert 200 == 404
