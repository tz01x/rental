from django.urls import path 
from .views import PropertyListApiView,PropertyTypeListApiView
app_name="mian_api"
urlpatterns = [
    path('property/list/',PropertyListApiView.as_view(),name="property_list"),
    path('propertytype/list/',PropertyTypeListApiView.as_view(),name="propertytype_list"),
]