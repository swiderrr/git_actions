import json
import pika
import os

try:
    credentials = pika.PlainCredentials(username=os.getenv('RABBITMQ_USER', 'guest'), password=os.getenv('RABBITMQ_PASSWORD', 'guest'))
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('RABBITMQ_HOST', 'localhost'), port=os.getenv('RABBITMQ_PORT', '5672'), credentials=credentials, heartbeat=0, blocked_connection_timeout=300))
    channel = connection.channel()
except Exception as err:
    print("Username: ")
    print(os.getenv('RABBITMQ_USER', 'guest'))
    print("Password: ")
    print(os.getenv('RABBITMQ_PASSWORD', 'guest'))
    print("Rabbit Host: ")
    print(os.getenv('RABBITMQ_HOST', 'guest'))
    print("Rabbit Port: ")
    print(os.getenv('RABBITMQ_PORT', 'guest'))

def publish(method, body):
    try:
        properties = pika.BasicProperties(method)
        channel.basic_publish(exchange='', routing_key=os.getenv('ROUTING_KEY', 'blue'), body=json.dumps(body), properties=properties)
        return 'published'
    except Exception as err:
        return err
