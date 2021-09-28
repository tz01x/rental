
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('',include('imguploading.urls')),
    path('',include('features.urls')),
    path('',include('main.urls')),
    path('',include('user.urls')),
    path('api/',include('imguploading.api.urls')),
    path('api/',include('main.api.urls')),
    path('api/',include('user.api.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
