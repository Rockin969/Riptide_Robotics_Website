from django.urls import path

from . import views

urlpatterns = [
    path("", views.Years_Home, name="years_index"),
    path("<int:year_id>", views.year, name="year"),
]