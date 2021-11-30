from rest_framework import serializers
from .models import BackendData

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendData
        fields = ['videoId', 'likes', 'dislikes', 'comments']
        depth = 1