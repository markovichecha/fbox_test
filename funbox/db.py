from time import time

import redis
from flask import current_app as app


def set_pool(host='localhost', port=6379, db=0):
    return redis.ConnectionPool(host=host, port=port, db=db, decode_responses=True)


def get_connection(pool):
    return redis.Redis(connection_pool=pool)


def store_domains(domains):
    with get_connection(app.config['DATABASE']) as r:
        creation_ts = int(str(time()).split('.')[0])
        key = 'domains:{}'.format(creation_ts)
        r.lpush(key, *domains)
        r.zadd('domains:time', {creation_ts: creation_ts}, nx=True)


def get_domains(from_ts, to_ts):
    with get_connection(app.config['DATABASE']) as r:
        creation_ts_keys = r.zrangebyscore('domains:time', min=from_ts, max=to_ts)
        if not creation_ts_keys:
            return
        domains = set()
        for creation_ts_key in creation_ts_keys:
            requested_domains = r.lrange('domains:{}'.format(int(creation_ts_key)), 0, -1)
            domains.update(requested_domains)
        return list(domains)
