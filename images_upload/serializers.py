from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "title",
            "image",
            "created_at",
        )
        model = Image
