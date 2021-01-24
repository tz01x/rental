
from  django.urls import path
from .views import *

urlpatterns=[
    path('district/',DistrictsListApi.as_view()),
    path('thana/',ThanaListApi.as_view()),
]