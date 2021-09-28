from  django.urls import path
from .views import *
from django.views.generic import TemplateView
app_name="main"
urlpatterns = [
    path("post-ad/create/",adPost.as_view(),name="create_adpost"),
    path("post-ad/<slug:slug>/update/",PostUpdate.as_view(),name="update_adpost"),
    path("post-ad/<slug:slug>/part-2/upate",adPostpart2,name="createAndupdate_adpost_p2"),
    path("post-ad/<slug:slug>/images-uplodaing/",imageUpload,name="createAndupdate_adpost_images"),
    path("property/details/<int:pk>/",PropertyDetailsView.as_view(),name="property_details"),
    path("property/details/<slug:slug>/",PropertyDetailsView.as_view(),name="property_details"),
    path("property/list/",PropertyListView.as_view(),name="property_list"),

    path("test/",TemplateView.as_view(template_name="main/test.html"),name=""),
    path("",homeView,name="home"),
    path("contact/",ContactView,name="contact"),
    path("privacypolicy/",PrivacyPolicyView,name="privacypolicy"),

]
