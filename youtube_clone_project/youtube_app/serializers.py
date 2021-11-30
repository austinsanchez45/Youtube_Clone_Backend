from rest_framework import serializers
from .models import BackendData
from .models import Comments

class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendData
        fields = ['videoId', 'likes', 'dislikes', 'comments']
        depth = 1
        
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['commentId', 'parentId', 'body', 'likes', 'dislikes']