from rest_framework import serializers

from .models import Property,PropertyType,FeatureType
from imguploading.serializers import ImageSerializer
class PropertySerializers(serializers.ModelSerializer):
    img=ImageSerializer(many=True)
    class Meta:
        model=Property 
        fields=[
        'slug',
        'title',
        'price',
        'bedroom',
        'bathroom',
        'property_size',
        'city',
        'area',
        'img',
        ]
class  PropertyTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model=PropertyType
        fields="__all__"
class  FeatureTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model=FeatureType
        fields=["name"]