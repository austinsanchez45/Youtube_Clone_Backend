from rest_framework import serializers
from .models import BackendData, Comments

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendData
        fields = ['videoId', 'likes', 'dislikes', 'comments']
    
    class Meta:
        model = Comments
        fields = ['commentId', 'parentId', 'body', 'likes', 'dislikes']