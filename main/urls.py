from  django.urls import path
from .views import *
from django.views.generic import TemplateView
app_name="main"
urlpatterns = [
    path("adpost/create/",adPost.as_view(),name="create_adpost"),
    path("adpost/p1/<int:pk>/update/",PostUpdate.as_view(),name="update_adpost"),
    path("adpost/p2/<int:pk>/",adPostpart2,name="createAndupdate_adpost_p2"),
    path("adpost/<int:pk>/images/",imageUpload,name="createAndupdate_adpost_images"),
    path("details/property/<int:pk>/details",PropertyDetailsView.as_view(),name="property_details"),
    path("list/",PropertyListView.as_view(),name="property_list"),

    path("test/",TemplateView.as_view(template_name="main/test.html"),name=""),
    path("",homeView,name="home"),
    path("contact/",ContactView,name="contact"),

]
