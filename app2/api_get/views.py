from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from consumer import *

@api_view(['GET'])
def index(request):
    return Response(status=status.HTTP_200_OK, data={'message': 'Success'})