from django.urls import path 
from .views import PropertyListApiView,PropertyTypeListApiView,FeatureTypeListApiView
app_name="mian_api"
urlpatterns = [
    path('property/list/',PropertyListApiView.as_view(),name="property_list"),
    path('property/types/list/',PropertyTypeListApiView.as_view(),name="propertytype_list"),
    path('property/features/list/',FeatureTypeListApiView.as_view(),name="featureTypelist"),
]