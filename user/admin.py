from django.contrib import admin

# Register your models here.
from .models import Profile,Citys#,Districts,Thana
admin.site.register(Profile)
admin.site.register(Citys)
# admin.site.register(Districts)
# admin.site.register(Thana)
