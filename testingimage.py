# import  cv2,numpy

# img=cv2.imread('./media/images/pexels-photo-2970375.jpeg')
# print(img.shape)

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,text='rental',org=(10,img.shape[0]-10), fontFace=font, fontScale=1,color=(255,255,255,0.5),thickness=1,lineType=cv2.LINE_AA)

# cv2.imwrite('./myimg.jpeg',img)
null=None


import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rental.settings')

import django
django.setup()
from user.models import Citys
from main.models import  PropertyType
import json

ptype=['Bachelor','Hostal','Apartment','Flat']
Citys.objects.all().delete()
PropertyType.objects.all().delete()
# Districts.objects.all().delete()
# Thana.objects.all().delete()
divisions=json.load(open('citys.json',encoding="utf8"))[0]['citys']
# districts=json.load(open('districts.json',encoding="utf8"))['districts']
# upazila=json.load(open('upazila.json',encoding="utf8"))['upazilas']
# print(upazila)
for p in ptype:
    PropertyType.objects.create(name=p)
for division in divisions:
    Citys.objects.create(name=division['name'],bn_name=division['bn_name'],lat=division['lat'],lng=division['long'])
    # print(p)
# last_div_id=None
# city=None
# division_name=None
# for district in districts:
#     curr_div_id=district['division_id']
#     if last_div_id != curr_div_id:
#         for i in divisions:
#             if i['id']==curr_div_id:
#                 division_name=i['name']
#                 break
#         city=Citys.objects.filter(name=division_name)[0]

#     obj=Districts(city=city,name=district['name'],bn_name=district['bn_name'],lat=district['lat'],lon=district['long'])
#     obj.save()
#     last_div_id=curr_div_id
# last_dis=None
# districts_obj=None
# for up in upazila:
#     curr_dis=up['district_id']
#     if last_dis!=curr_dis:
#         divisions_name=None
#         for dis in districts:
#             if curr_dis==dis['id']:
#                 divisions_name=dis['name']
#                 print(divisions_name)
#                 break
#         districts_obj=Districts.objects.filter(name=divisions_name)[0]

#     up_opj=Thana.objects.create(city=districts_obj.city,districts=districts_obj,name=up['name'],bn_name=up['bn_name'])
#     last_dis=curr_dis



# print(Thana.objects.count())
