from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="home"),
    path("Preview/<str:pk>", views.preview, name="Preview"),
    path("delete_img/<str:pk>", views.delete_img, name="delete_img")
]