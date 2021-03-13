from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
import  json
from .forms import *
from .models import *
from django.views.generic import  DeleteView
from PIL import Image
# import numpy as np
from  PIL import ImageDraw
# import cv2 ,uuid,sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
# Create your views here.
def hotel_image_view(request):
    
    
#     print(translation.get_language())
#     translation.activate('bd')
#     if request.method == 'POST':


#         form = HotelForm(request.POST,request.FILES)
#         files=request.FILES.getlist('images')#from field name 'photos'

#         print(files)
#         if form.is_valid():
#             hotelobj=Hotel(name=form.cleaned_data['name'])
#             hotelobj.save()


#             # here every files are InMemoryUploadedFile type object

#             for imfile in files:
#                 # do sometion with the image

#                 img=Image.open(imfile)
#                 imgarr=np.array(img)
#                 # cvimge=cv2.cvtColor(imgarr,cv2.COLOR_BGR2RGB)
#                 cvimge=cv2.cvtColor(imgarr,cv2.COLOR_RGB2RGBA)
#                 # print(cvimge)
#                 cvimge=cv2.resize(cvimge,(100,100))
#                 # convert : cv2 to plt
#                 pltimg=Image.fromarray(cvimge)

#                 # createing a buffer to strore the image
#                 output=BytesIO()
#                 # load the output with the image data
#                 pltimg.save(output,format='png',quality=60)
#                 # createing unique file name
#                 filename=f"{uuid.uuid4()}.png"
#                 # making InMemoryUploadedFile for saving the file
#                 imgfile=InMemoryUploadedFile(output,'ImageField', filename, 'png', sys.getsizeof(output), None)


#                 img=Images(baseimage=imgfile)
#                 img.save()
#                 hotelobj.images.add(img)


#         else:
#             print(form.errors)
#             print('not valid ')

#         #     form.save()
#         #     if request.POST.get('isXhr')=="false":
#         #
#         #         return redirect('imguploading:here')
#         #     else:
#         #         data=[{'data':'__','success':True}]
#         #
#         #         return HttpResponse(json.dumps(data))
#     else:
#         form = HotelForm()
    # objs=Hotel.objects.all().order_by("-id")
    return render(request, 'home.html')

def ImageDelete(request,pk,objpk):
    object=get_object_or_404(Images,pk=pk)
    object.delete()
    return redirect('main:adpostimg',pk=objpk)
