from django.shortcuts import render
from .models import History

# Create your views here.

def History_Home(request):
    return render(request, "History/History_Home.html", {
        "histories": History.objects.all()
    })