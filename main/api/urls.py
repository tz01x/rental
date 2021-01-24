from django.urls import path 
from .views import PropertyListApiView
app_name="mian_api"
urlpatterns = [
    path('property/list/',PropertyListApiView.as_view(),name="property_list"),
]