from django.urls import path,include,reverse_lazy
from .views import  *
app_name='imguploading_api'
urlpatterns = [
        path('image/delete/<int:pk>/',ImageDelete.as_view(),name='deleteimg'),
    ]
