import uuid, requests

SITE = "https://quickpizza.grafana.com"
s = requests.Session()
user = {"username": "lab-" + uuid.uuid4().hex[:12], "password": "Pizza-2026"}
s.post(SITE + "/api/users", json=user)
token = s.post(SITE + "/api/users/token/login", json=user).json()["token"]
auth = {"Authorization": "token " + token}
pid = s.post(SITE + "/api/pizza", json={}, headers=auth).json()["pizza"]["id"]

cases = {
    "C2 decimal":   ({"pizza_id": pid, "stars": 3.5}, auth),
    "C2 text":      ({"pizza_id": pid, "stars": "3"}, auth),
    "C2 missing":   ({"pizza_id": pid}, auth),
    "C3 no pizza":  ({"pizza_id": 999999999, "stars": 3}, auth),
    "C4 no token":  ({"pizza_id": pid, "stars": 3}, None),
    "C4 short":     ({"pizza_id": pid, "stars": 3},
                     {"Authorization": "token short"}),
}
for name, (body, headers) in cases.items():
    r = s.post(SITE + "/api/ratings", json=body, headers=headers)
    print(name, r.status_code, r.text)