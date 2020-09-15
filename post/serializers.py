from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
  category = serializers.StringRelatedField()
  user = serializers.StringRelatedField()
  class Meta:
    model = Post
    fields = ('id', 'title', 'content', 'category', 'user', 'create_at')