
from  django.urls import path
from .views import *

urlpatterns=[
    path('city/<str:name>/',CitysListApi.as_view()),
    # path('thana/',ThanaListApi.as_view()),
]