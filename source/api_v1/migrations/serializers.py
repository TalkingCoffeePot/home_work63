from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from feed.models import PostModel

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id', 'image', 'text', 'likes', 'date_add']
        read_only_fields = ['user']

