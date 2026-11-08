import requests

SITE = "https://quickpizza.grafana.com"

# The list of pizza names answers 200 and holds Margherita.
def test_names_are_listed():
    res = requests.get(SITE + "/api/names")
    assert res.status_code == 200
    assert "Pineapple Supreme" in res.json()["names"]