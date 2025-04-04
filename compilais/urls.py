from django.urls import path
from compilais import views

urlpatterns = [
    path('', views.index, name="index"),
    path('courses/', views.courses, name="courses"),
    path('plans/', views.plans, name="plans"),
    path('dashboard/', views.dashboard, name="dashboard"),
]