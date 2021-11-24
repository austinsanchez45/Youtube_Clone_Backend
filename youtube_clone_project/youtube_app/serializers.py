from rest_framework import serializers
from .models import Comment

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'videoId', 'userComment', 'like', 'dislike']