from django.urls import path ,include
from . import views

urlpatterns = [
    path("", views.p_view, name="p_view"), 
    path("rec", views.r_view, name="r_view"), 
    path("ad", views.a_view, name="a_view"), 
    path("log", views.log, name="login"), 
    ]

