from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Comment
from .serializers import YoutubeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class YoutubeList(APIView):
    
    def get(self, request):
        youtube = Comment.objects.all()
        serializer = YoutubeSerializer(youtube, many = True)
        return Response(serializer.data)