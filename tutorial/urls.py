from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtopic/', views.addtopic, name="addtopic"),
    path('cplusplus/', views.cplusplus, name="cplusplus"),
]