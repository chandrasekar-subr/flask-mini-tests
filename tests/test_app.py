import json


def test_status_code(app, client):
    del app
    res = client.get('/empdb/employee')
    assert res.status_code == 200
    # expected = {'hello': 'world'}
    # assert expected == json.loads(res.get_data(as_text=True))
