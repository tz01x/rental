from user.serializers import  DistrictsSerializers,DistrictsSerializers_Bn,ThanaSerializers
from user.models import Citys,Districts
from rest_framework.generics import ListAPIView

class  DistrictsListApi(ListAPIView):
    serializer_class=DistrictsSerializers
    def get_queryset(self):
        try:
            isbn=self.request.GET.get('bn',None)
            city=self.request.GET.get('city',None)
            qs=Citys.objects.filter(name=city).first().district.all()
            if isbn !=None:
                self.serializer_class=DistrictsSerializers_Bn
            
            return qs
        except:
            return Citys.objects.none()
class ThanaListApi(ListAPIView):
    serializer_class=ThanaSerializers
    def get_queryset(self):
        _district=self.request.GET.get('district',None)
        if _district!=None:
            try:
                district_obj=Districts.objects.filter(name=_district).first()
                if district_obj:
                    return district_obj.thana.all()
            except:
                pass
            
        return Districts.objects.none()
        


            
        
