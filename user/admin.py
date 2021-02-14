from django.contrib import admin

# Register your models here.
from .models import Profile,Citys,Messages#,Districts,Thana
admin.site.register(Profile)
admin.site.register(Messages)
admin.site.register(Citys)
# admin.site.register(Districts)
# admin.site.register(Thana)
