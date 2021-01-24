from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys,os
import datetime
import cv2,numpy

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from django.conf import settings
import uuid
# Create your models here.

def getB_path(instance,filename):
    base,ext=os.path.splitext(filename)
    filename = "%s.%s" % (uuid.uuid4(), ext[1:])
    return os.path.join('images/', filename)
def getT_path(instance,filename):
    base,ext=os.path.splitext(filename)
    filename = "%s.%s" % (uuid.uuid4(), ext[1:])
    return os.path.join('timages/', filename)
    
class Images(models.Model):

    baseimage=models.ImageField(upload_to=getB_path,null=True,blank=True)
    timage=models.ImageField(upload_to=getT_path,null=True,blank=True)
    
    
    def save(self):
        self.timage=self.baseimage
        baseimage = Image.open(self.baseimage).convert("RGBA")
        baseimage=baseimage.resize((400,400))
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new('RGBA', baseimage.size, (255,255,255,0))

        # get a font
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype(os.path.join(settings.BASE_DIR,"./static/static_dir/font/Epilogue-BoldItalic.ttf"),16)
        txt_width,txt_height=font.getsize('rental.bd.com')
        draw = ImageDraw.Draw(txt)
        # print(baseimage.size)


        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text(((baseimage.width//2)-(txt_width//2), baseimage.height-50),"rental.bd.com","rgba(255,255,255,128)",font=font)
        outimg = Image.alpha_composite(baseimage, txt)

        output = BytesIO()

        #Resize/modify the image
        # im = im.resize( (200,200) )


        f={
        'jpeg':'JPEG',
        'png':'PNG',
        'jpg':'JPEG',
        }
        #filename , .jpg
        name, extension = os.path.splitext(self.baseimage.name)
        # print(name,extension[1:])

        #after modifications, save it to the output
        outimg.save(output,'png', quality=60)
        output.seek(0)
        #change the imagefield value to be the newley modifed image value
        imgname="img-%s%s"%(str(datetime.datetime.now().timestamp()).split('.')[0],'.png')
        # print(imgname)
        self.timage = InMemoryUploadedFile(output,'ImageField', imgname, 'png', sys.getsizeof(output), None)

        super(Images,self).save()
    def delete(self, using=None, keep_parents=False):
       
        storage = self.baseimage.storage

        if storage.exists(self.baseimage.name):
            storage.delete(self.baseimage.name)

        storage = self.timage.storage
        if storage.exists(self.timage.name):
            storage.delete(self.timage.name)

        super().delete()


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    # hotel_Main_Img = models.ImageField(upload_to='images/')
    # timg=models.ImageField(upload_to="timg/")
    images=models.ManyToManyField(Images,related_name='multipleImages')

    def __str__(self):
        return self.name
    def save(self):
        super(Hotel,self).save()
