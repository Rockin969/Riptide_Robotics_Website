from django.urls import path

from . import views

urlpatterns = [
    path("", views.Instructors_Home, name="inst_index")
]