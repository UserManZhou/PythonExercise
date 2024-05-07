from . import views
from django.urls import path

urlPatterns = [
    path("", views.index, name="index")
]
