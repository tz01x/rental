from django.urls import path,include,reverse_lazy
from .views import  *
app_name='imguploading'
urlpatterns = [
        path('image/upload/test/',hotel_image_view,name='here'),
        path('images/delete/<int:pk>/<int:objpk>/',ImageDelete,name='del_img')

    ]
# while True:
        #     if txt_width<baseimage.width:
        #         break
        #     else:
        #         inital_font_size-=1
        #         font = ImageFont.truetype(os.path.join(settings.BASE_DIR,"./static/static_dir/font/Epilogue-BoldItalic.ttf"),inital_font_size)
        #         txt_width,txt_height=font.getsize('rental.bd.com')