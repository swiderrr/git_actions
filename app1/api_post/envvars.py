import os

CONFIG = {
    'app1_hostname' : os.getenv('APP1_HOST', 'localhost'),
    'rabbit_username' : os.getenv('RABBITMQ_USER', 'guest'),
    'app1_port' : os.getenv('APP1_PORT', '8080'),
    'rabbit_password' : os.getenv('RABBITMQ_PASSWORD', 'guest'),
    'rabbit_host' : os.getenv('RABBITMQ_HOST', 'localhost'),
    'rabbit_port' : os.getenv('RABBITMQ_PORT', '5672'),
    'routing_key' : os.getenv('ROUTING_KEY', 'blue')
}