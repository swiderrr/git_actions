import pytest
import redis
import json
from app2.app2.settings import CONFIG
from app2.consumer import redis_client, connection, callback



def test_redis_connection():
    assert redis_client.ping() == True



def test_rabbitmq_connection():
    assert connection.is_open == True


def test_set_new_key():
    redis_client = redis.Redis(host=CONFIG['redis_host'], port=CONFIG['redis_port'], db=0)
    obj = {
        'first_name': 'Test_first_name',
        'last_name': 'Test_last_name',
    }
    a = callback(ch='blue', method='post', properties='', body=json.dumps(obj))
    assert a == True
