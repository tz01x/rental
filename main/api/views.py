from main.serializers import PropertySerializers,PropertyTypeSerializers,FeatureTypeSerializers
from main.models import Property,PropertyType,FeatureType
from rest_framework.generics import ListAPIView
from  rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.db.models import Q

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20

    
class PropertyListApiView(ListAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class=PropertySerializers
    pagination_class=StandardResultsSetPagination
    # queryset=Property.objects.all()
    # city=Chattogram&property_type=Flat&price=5000,10000&bedroom=5&bathroom=4&features=play%20gound,24/7%20security

    def get_queryset(self):
        qs=Property.objects.filter(varified=True,publish=True)
        id=self.getData('id')
        slug=self.getData('slug')
        title=self.getData('title')
        city=self.getData('city')
        property_type=self.getData('property_type')
        price=self.getData('price')
        bedroom=self.getData('bedroom')
        bathroom=self.getData('bathroom')
        features=self.getData('features')

        # print(title,city,property_type,price)
        
    

        if id:
            qs=qs.filter(id=id)
        if id is None and slug:
            qs=qs.filter(slug=slug)
        if id and slug is None and title:
            qs=qs.filter(title__icontains=title)
        if city:
            qs=qs.filter(city__icontains=city)
        if price:
            qs=qs.filter(price__range=(price.split(",")))
        if bedroom:
            if int(bedroom)<5:
                qs=qs.filter(bedroom=bedroom)
            else:
                qs=qs.filter(bedroom__gte=bedroom)
        
        

        if bathroom:
            if int(bathroom)<5:
                qs=qs.filter(bathroom=bathroom)
            else:
                qs=qs.filter(bathroom__gte=bathroom)


        if features:
            
            fs=FeatureType.objects.filter(name__in=features.split(','))
            qs=qs.filter(feature_types__in=fs)
        return qs.distinct()

    def getData(self,name):
        return self.request.GET.get(name,None)
class PropertyTypeListApiView(ListAPIView):
    serializer_class=PropertyTypeSerializers
    def get_queryset(self):
        
        return PropertyType.objects.all()
class FeatureTypeListApiView(ListAPIView):
    serializer_class=FeatureTypeSerializers
    def get_queryset(self):
        return FeatureType.objects.all()

