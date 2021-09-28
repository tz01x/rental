from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
import re 
# from phonenumber_field.modelfields import PhoneNumberField #<---
from django.conf import settings
class Messages(models.Model):
    user=models.ForeignKey(to=User,related_name="message",on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    msg=models.TextField(max_length=1000)
    created=models.DateTimeField(auto_now_add=True)
    viewed=models.BooleanField(default=False)
    def __str__(self):
        return self.name+", has send you a message "

    def message(self):
        return self.msg.split(',')[0]
    def gePropertyLink(self):
        msgs=self.msg.split(',')
        link=msgs[-1]
        if re.match(r'((http://)|(https://))([0-9a-z]+.)+',link):
            return link[-1]
        return None

    class Meta:
        ordering=('-created',)
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=360, blank=True)
    area = models.CharField(max_length=360, blank=True)
    phone = models.CharField(blank=True,max_length=16)
    email_confirmed = models.BooleanField(default=False)
    ps=models.CharField(blank=True,null=True,max_length=499)
    gender=models.CharField(choices=[('m',"Male"),('f','Female'),('o',"Other")],max_length=1,blank=True)
    jobDescription=models.CharField(max_length=150,blank=True,null=True)
    companyName=models.CharField(max_length=150,blank=True,null=True)
    fb_link=models.CharField(max_length=500,blank=True,null=True)
    yt_link=models.CharField(max_length=500,blank=True,null=True)
    web_link=models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Citys(models.Model):
    name=models.CharField(max_length=150,blank=True)
    bn_name=models.CharField(max_length=150,blank=True,null=True)
    lat=models.CharField(max_length=50,blank=True)
    lng=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return f'{self.id} {self.name}'
    def bn(self):
        return self.bn_name

# class Districts(models.Model):
#     city=models.ForeignKey('Citys',on_delete=models.CASCADE,related_name='district')
#     name=models.CharField(max_length=150,blank=True)
#     bn_name=models.CharField(max_length=150,blank=True,null=True)
#     lat=models.CharField(max_length=50,blank=True)
#     lon=models.CharField(max_length=50,blank=True)
#     def __str__(self):
#         return f'{self.name}'
#     def bn(self):
#         return self.bn_name
# class Thana(models.Model):
#     city=models.ForeignKey('Citys',on_delete=models.CASCADE,related_name='thana',null=True,blank=True)
#     districts=models.ForeignKey('Districts',on_delete=models.CASCADE,related_name='thana')
#     name=models.CharField(max_length=150,blank=True)
#     bn_name=models.CharField(max_length=150,blank=True,null=True)
#     lat=models.CharField(max_length=50,blank=True)
#     lon=models.CharField(max_length=50,blank=True)
#     def __str__(self):
#         return f'{self.name}'
#     def bn(self):
#         return self.bn_name
    
    


