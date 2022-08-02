import pytest
from app1.settings import CONFIG
import requests
from api_post.producer import publish, channel


def test_osenv():
    conf_vars = [v for v in CONFIG.values()]
    assert all(conf_vars)

def test_rabbitmq_connection():
    assert channel.is_open == True

def test_rabbitmq_publish():
    obj = {
        'first_name': 'Test_first_name',
        'last_name': 'Test_last_name',
    }
    assert publish('post', obj) == "published"

def test_400resp():
    url = "http://" + CONFIG["app1_hostname"] + ":" + CONFIG["app1_port"] + "/add"
    obj = "Definitely not a json"
    response = requests.post(url, json=obj)
    assert response.status_code == 400
#
def test_200resp():
    url = "http://" + CONFIG["app1_hostname"] + ":" + CONFIG["app1_port"] + "/add"
    obj = {
        'first_name': 'Test_first_name',
        'last_name': 'Test_last_name',
    }
    response = requests.post(url, json = obj)
    assert response.status_code == 200

