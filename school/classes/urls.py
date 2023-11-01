#it's advisable to give your apps a default path too
#there can only be one default path per project and also per app

from django.urls import path, include

from . import views

app_name = "classes"


urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('add', views.add, name="add"),
    path('viewdata', views.viewdata, name="viewdata")
]