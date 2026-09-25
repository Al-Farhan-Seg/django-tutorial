from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("al-farhan", views.al_farhan, name="al-farhan")
]