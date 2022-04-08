from django.shortcuts import render
from datetime import datetime

from .models import Blog

#Create your views here.

def Blog_Home(request):
    return render(request, "Blog/Blog_Home.html", {
        "blogs": Blog.objects.all()
    })

def blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, "Blog/Blog_Layout.html", {
        "blog": blog
    })