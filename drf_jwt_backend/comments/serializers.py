from rest_framework import serializers
from .models import Comment, Reply

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id','video_id', 'text', 'likes', 'dislikes', 'user_id']


class ReplySerializer(serializers.ModelSerializer):
  class Meta:
    model = Reply
    fields = ['id','text', 'comment_id', 'user_id']
