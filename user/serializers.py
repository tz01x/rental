from rest_framework import serializers

from user.models import  Districts,Thana

class DistrictsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Districts
        fields=['name']

class DistrictsSerializers_Bn(serializers.ModelSerializer):
    class Meta:
        model=Districts
        fields=['bn_name']

class ThanaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Thana
        fields=['name']
