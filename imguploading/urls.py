from django.urls import path,include,reverse_lazy
from .views import  *
app_name='imguploading'
urlpatterns = [
        path('image/upload/test/',hotel_image_view,name='here'),
        path('images/delete/<int:pk>/<int:objpk>/',ImageDelete,name='del_img')

    ]
