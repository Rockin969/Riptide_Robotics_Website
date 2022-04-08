from django.urls import path

from . import views

urlpatterns = [
    path("", views.Blog_Home, name="blog_index"),
    path("<int:blog_id>", views.blog, name="blog"),
]
