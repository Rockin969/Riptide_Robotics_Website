from django.urls import path

from . import views

urlpatterns = [
    path("", views.History_Home, name="his_index")
]