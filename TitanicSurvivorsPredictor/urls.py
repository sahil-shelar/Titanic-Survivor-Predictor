from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("result",views.result),
    path('back_to_index', views.back_to_index, name='back_to_index'),
]