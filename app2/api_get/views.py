from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from consumer import *

print("Username: ")
print(CONFIG['rabbit_username'])
print("Password: ")
print(CONFIG['rabbit_password'])
print("Rabbit Host: ")
print(CONFIG['rabbit_host'])
print("Rabbit Port: ")
print(CONFIG['rabbit_port'])

channel.basic_consume(queue='blue', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()

@api_view(['GET'])
def index(request):
    return Response(status=status.HTTP_200_OK, data={'message': 'Success'})