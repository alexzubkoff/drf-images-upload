from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    # thumbnail_small_url = serializers.ReadOnlyField()
    # thumbnail_large_url = serializers.ReadOnlyField()

    class Meta:
        fields = (
            'id',
            'user',
            'title',
            'image',
            # 'thumbnail_small_url',
            # 'thumbnail_large_url',
            'created_at',
        )
        model = Image
