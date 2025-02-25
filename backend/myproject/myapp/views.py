from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp.serializers import *

def home(request):
    return HttpResponse("Hello AWS, World!")

@api_view(['POST'])
def image_upload(request):
    serializer = UploadedImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Image uploaded successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)