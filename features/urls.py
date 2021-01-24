
from django.urls import path,include
from .views import *
app_name="features"
urlpatterns = [
    path('features/<int:pk>/create',featureFormsView,name="featuresfrom"),
    path('catagory',allCtagory.as_view(),),
    path('feature/<int:pk>/update',updateFeature.as_view(),name='featureupdate')

]
