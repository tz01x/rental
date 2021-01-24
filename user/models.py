from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
# from phonenumber_field.modelfields import PhoneNumberField #<---
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=360, blank=True)
    area = models.CharField(max_length=360, blank=True)
    phone = models.CharField(blank=True,max_length=16)
    email_confirmed = models.BooleanField(default=False)
    ps=models.CharField(blank=True,null=True,max_length=499)
    gender=models.CharField(choices=[('m',"Male"),('f','Female'),('o',"Other")],max_length=1,blank=True)
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
    lon=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return f'{self.id} {self.name}'
    def bn(self):
        return self.bn_name

class Districts(models.Model):
    city=models.ForeignKey('Citys',on_delete=models.CASCADE,related_name='district')
    name=models.CharField(max_length=150,blank=True)
    bn_name=models.CharField(max_length=150,blank=True,null=True)
    lat=models.CharField(max_length=50,blank=True)
    lon=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return f'{self.name}'
    def bn(self):
        return self.bn_name
class Thana(models.Model):
    city=models.ForeignKey('Citys',on_delete=models.CASCADE,related_name='thana',null=True,blank=True)
    districts=models.ForeignKey('Districts',on_delete=models.CASCADE,related_name='thana')
    name=models.CharField(max_length=150,blank=True)
    bn_name=models.CharField(max_length=150,blank=True,null=True)
    lat=models.CharField(max_length=50,blank=True)
    lon=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return f'{self.name}'
    def bn(self):
        return self.bn_name
    
    


