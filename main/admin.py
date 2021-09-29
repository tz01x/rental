from django import urls
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
from .models import *
from .forms import FeatureForm

admin.site.register(PropertyType)
admin.site.register(PropertyCategory)
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id",'title', "varified",'created','viewproperty_link')
    list_filter = ("created", )
    search_fields = ("title__startswith",'description_startswith','city_startswith' )
    def viewproperty_link(self,obj):
        url=reverse("main:property_details",kwargs={'slug':obj.slug})
        return format_html( ' <a href="{0}" target="_blank" >View</a> ',url)
    viewproperty_link.short_description ="property link"
admin.site.register(Utilities)
admin.site.register(Preference)
admin.site.register(Contact)


class FeatureTypeAdmin(admin.ModelAdmin):
    form=FeatureForm
    

admin.site.register(FeatureType,FeatureTypeAdmin)
