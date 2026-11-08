import pytest

# Boundary values for stars: 1 and 5 are saved, 0 and 6 are refused unchanged.
@pytest.mark.parametrize("stars, expected", [(0, 400), (1, 200), (5, 200), (6, 400)])
def test_update_stars_boundaries(api, auth, rating, stars, expected):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected

    saved = api.get(path, headers=auth).json()["stars"]
    if expected == 200:
        assert saved == stars
    else:
        assert saved == rating["stars"]