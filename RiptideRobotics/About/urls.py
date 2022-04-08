from django.urls import path

from . import views

urlpatterns = [
    path("", views.About_Home, name="abt_index")
    
]
