from rest_framework import serializers
from image_api.models import Image

class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    image_url = serializers.URLField()
    description = serializers.CharField()

    def create(self, data):
        return Image.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.image_url = data.get('image_url', instance.image_url)
        instance.description = data.get('description', instance.description)

        instance.save()
        return instance
