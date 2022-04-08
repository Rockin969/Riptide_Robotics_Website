from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def About_Home(request):
    return render(request, "About/About_Layout.html")