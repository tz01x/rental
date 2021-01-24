from django.db import models
from django.conf import settings
from imguploading.models import Images
import json
class PropertyType(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class PropertyCategory(models.Model):
    name=models.CharField(max_length=100)
    property_types=models.ManyToManyField(PropertyType,related_name="property_catagory_types",blank=True)
    def __str__(self):
        return self.name


class Property(models.Model):
    adfor=[
    ('Rent','Rent'),
    ('sale','Sale'),
    ]
    user=models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    
    title=models.CharField(max_length=10000)
    description=models.CharField(max_length=15000,blank=True,null=True)
    # propertry_built

    available_from=models.DateField(editable=True,null=True)
    city=models.CharField(max_length=400,blank=True,null=True)
    area=models.CharField(max_length=400,blank=True,null=True,verbose_name='District')
    thana=models.CharField(max_length=400,blank=True,null=True,verbose_name='Thana')
    latlong=models.CharField(max_length=100,blank=True,null=True)
    adress=models.CharField(max_length=400,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    # post_status 
    publish=models.BooleanField(choices=[(True,'Publish'),(False,'Arcive')],default=False,verbose_name="Post Status")

    email=models.EmailField(blank=True,null=True)
    contact_person=models.CharField(max_length=15,blank=True,null=True)
    # property_category=models.ForeignKey(to="PropertyCategory",on_delete=models.CASCADE)
    property_types=models.ForeignKey(to="PropertyType",related_name="property_types",on_delete=models.SET_NULL,null=True)
    ad_for=models.CharField(max_length=4,choices=adfor,blank=True,null=True,verbose_name="Property AD type")
    # roommate_type=>male , female ,any
    roommate_type=models.CharField(choices=[('any','Any'),('male','Male'),('female','Female'),],max_length=6,blank=True,null=True)
    # if property_type is hostal ---> hostal_type>Boys hostal , girsl hostal 
    hostal_type=models.CharField(max_length=11,choices=[('girl hostal','Girl Hostal'),('boy hostal','Boy Hostal')],blank=True,null=True)
    # member per room  
    people_per_room=models.IntegerField(blank=True,null=True,verbose_name="person per room")
    advance_payment=models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    # property specification
    property_size=models.FloatField(blank=True,null=True,verbose_name="property size in sqft")
    bedroom=models.IntegerField(default=0)
    living_room=models.IntegerField(default=0)
    drawing_room=models.IntegerField(default=0)
    bathroom=models.IntegerField(default=0)
    kitchen=models.IntegerField(default=0)
    balcony=models.IntegerField(default=0)
    parking_space=models.BooleanField(default=False)

    # features
    feature_types=models.ManyToManyField("FeatureType",related_name="property_features",null=True,blank=True)
    utility_bill=models.ManyToManyField('Utilities',related_name="utility_bill",null=True,blank=True)
    set_available=models.CharField(max_length=250,blank=True,null=True)

    preference=models.ManyToManyField('Preference',related_name='properties')
    img=models.ManyToManyField(Images,related_name='properties')
    youtube_link=models.URLField(blank=True,null=True)
    class Meta:
        ordering=['-id','-created']

    def __str__(self):
        return f"#id: {self.id} :/ {self.title} "
    def getAdfor(self):
        try:
            return self.ad_for.title
        except:
            return ''
    def getLatLong(self):

        if self.latlong!=None or len(self.latlong)>1:
            latlng=self.latlong.split(',')
            # print(latlng)
            try:
                data={
                    'lat':latlng[0],
                    'lng':latlng[1]
                }
                return json.dumps(data)
                
            except:
                pass
        
        return '{"lat":"","lng":""}'




class FeatureType(models.Model):
    ptype=models.ManyToManyField(PropertyType,related_name="feature_type")
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name
class Utilities(models.Model):
    name=models.CharField(max_length=250)
    ptype=models.ManyToManyField(PropertyType,related_name="utilities")
    def __str__(self):
        return self.name

class Preference(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name
