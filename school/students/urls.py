
from django.urls import path
from . import views

app_name = "students"
urlpatterns = [
    path('students', views.Home, name= "Home")

]