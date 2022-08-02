from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from api_post.producer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from api_post.producer import publish


@csrf_exempt
@api_view(['POST'])
def PostView(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            publish('post', data)
            return JsonResponse(data)
        except:
            resp = {"Error message":"invalid request body"}
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)

