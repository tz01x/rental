from user.serializers import  CitysSerializers#,DistrictsSerializers_Bn,ThanaSerializers
from user.models import Citys
from rest_framework.generics import ListAPIView

class  CitysListApi(ListAPIView):
    serializer_class=CitysSerializers
    def get_queryset(self):
        try:
            city_name=self.kwargs.get('name',None)
            
            if city_name:
                qs=Citys.objects.filter(name__contains=city_name) 
                
                return qs
            else:
                return Citys.objects.all()
        except:
            return Citys.objects.none()
# class ThanaListApi(ListAPIView):
#     serializer_class=ThanaSerializers
#     def get_queryset(self):
#         _district=self.request.GET.get('district',None)
#         if _district!=None:
#             try:
#                 district_obj=Districts.objects.filter(name=_district).first()
#                 if district_obj:
#                     return district_obj.thana.all()
#             except:
#                 pass
            
#         return Districts.objects.none()
        


            
        
