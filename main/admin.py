from django.contrib import admin

# Register your models here.
from .models import *
from .forms import FeatureForm

admin.site.register(PropertyType)
admin.site.register(PropertyCategory)
admin.site.register(Property)
admin.site.register(Utilities)
admin.site.register(Preference)


class FeatureTypeAdmin(admin.ModelAdmin):
    form=FeatureForm
    

admin.site.register(FeatureType,FeatureTypeAdmin)
