from main.serializers import PropertySerializers,PropertyTypeSerializers
from main.models import Property,PropertyType
from rest_framework.generics import ListAPIView

class PropertyListApiView(ListAPIView):
    serializer_class=PropertySerializers
    # queryset=Property.objects.all()
    def get_queryset(self):
        qs=Property.objects.all()
        id=self.request.GET.get('id',None)
        title=self.request.GET.get('title',None)

        if id:
            qs=qs.filter(id=id)
        if id:
            qs=qs.filter(title=title)
        return qs
class PropertyTypeListApiView(ListAPIView):
    serializer_class=PropertyTypeSerializers
    def get_queryset(self):
        return PropertyType.objects.all()

