from rest_framework import serializers

from user.models import Citys

class CitysSerializers(serializers.ModelSerializer):
    class Meta:
        model=Citys
        fields=['name','bn_name','lat','lng']

# class DistrictsSerializers_Bn(serializers.ModelSerializer):
#     class Meta:
#         model=Districts
#         fields=['bn_name']

# class ThanaSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Thana
#         fields=['name']
