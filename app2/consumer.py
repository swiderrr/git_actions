import json
import pika
import redis
import datetime
import os



credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USER', 'guest'), password=os.getenv('RABBITMQ_PASSWORD', 'guest'))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('RABBITMQ_HOST', 'localhost'), port=os.getenv('RABBITMQ_PORT', '5672'), heartbeat=0, blocked_connection_timeout=300, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue=os.getenv('CONSUMER_QUEUE', 'blue'))

redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=int(os.getenv('REDIS_PORT', '6379')), db=0)
def callback(ch, method, properties, body):
    print("Received in api_get...")
    try:
        data = json.loads(body)
        time = str(datetime.datetime.now())
        return redis_client.setex(time, 60, json.dumps(data))
    except Exception as err:
        return err

channel.basic_consume(queue=os.getenv('CONSUMER_QUEUE', 'blue'), on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()