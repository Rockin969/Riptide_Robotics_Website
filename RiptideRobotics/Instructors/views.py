from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Instructors_Home(request):
    return render(request, "Instructors/Instructors_Layout.html")