from django.urls import path
from compilais import views

urlpatterns = [
    path('', views.index),
]