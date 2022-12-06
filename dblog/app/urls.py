"""basic urls for app"""
from django.urls import path
from app import views

urlpatterns = [
    path('',view=views.index,name="index"),
    path("documents/", view=views.documents, name="documents"),
]
