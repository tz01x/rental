from rest_framework import serializers

from .models import Property,PropertyType
from imguploading.serializers import ImageSerializer
class PropertySerializers(serializers.ModelSerializer):
    img=ImageSerializer(many=True)
    class Meta:
        model=Property 
        fields=[
        'title',
        'description',
        'available_from',
        'city',
        'area',
        'adress',
        'img',
        ]
class  PropertyTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model=PropertyType
        fields="__all__"