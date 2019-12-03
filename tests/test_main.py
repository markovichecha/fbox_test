import json
from time import time


def test_domains_processing(client):
    current_ts = int(str(time()).split('.')[0])

    response = client.post('/visited_links', json={
        'links': [
            'https://ya.ru',
            'https://ya.ru?q=123',
            'funbox.ru',
            'https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor'
        ]
    })
    json_data = json.loads(response.data)

    assert 'status' in json_data
    assert json_data['status'] == 'ok'

    from_ts = current_ts - 10
    to_ts = current_ts + 10

    response = client.get('/visited_domains?from={}&to={}'.format(from_ts, to_ts))
    json_data = json.loads(response.data)

    assert 'status' in json_data
    assert json_data['status'] == 'ok'
    assert 'domains' in json_data
    assert 'ya.ru' in json_data['domains']
    assert 'funbox.ru' in json_data['domains']
    assert 'stackoverflow.com' in json_data['domains']


def test_handlers_data_validation(client):
    response = client.post('/visited_links', json={'links': []})
    json_data = json.loads(response.data)

    assert 'status' in json_data
    assert json_data != 'ok'

    response = client.post('/visited_links', json={'inks': []})
    json_data = json.loads(response.data)

    assert 'status' in json_data
    assert json_data != 'ok'

    response = client.get('/visited_domains?to=from&from=to')
    json_data = json.loads(response.data)

    assert 'status' in json_data
    assert json_data != 'ok'