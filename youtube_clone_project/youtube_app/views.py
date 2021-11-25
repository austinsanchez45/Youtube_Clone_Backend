from functools import partial
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Comment
from .serializers import YoutubeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from youtube_clone_project.youtube_app import serializers

# Create your views here.

class YoutubeList(APIView):
    
    def get(self, request):
        youtube = Comment.objects.all()
        serializer = YoutubeSerializer(youtube, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = YoutubeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class Comments(APIView):
    
    def get(self, request, pk):
        comment = self.get_Comment(pk)
        serializer = YoutubeSerializer(comment)
        return Response(serializer.data)
    
    def get_Comment(self, pk):
        try:
            return Comment.objects.get(pk = pk)
        except:
            raise Http404
        
    def put(self, request, pk):
        comment = self.get_Comment(pk)
        serializer = YoutubeSerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment = self.get_Comment(pk)
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class Like(APIView):
    
    def get_Comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except:
            raise Http404    
    
    def patch(self, request, pk):
        comment = self.get_Comment(pk)
        comment.like += 1
        serializer = YoutubeSerializer(comment, data = request.data, partial = True)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class Dislike(APIView):
    
    def get_Comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except:
            raise Http404    
    
    def patch(self, request, pk):
        comment = self.get_Comment(pk)
        comment.dislike += 1
        serializer = YoutubeSerializer(comment, data = request.data, partial = True)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    