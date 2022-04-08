from django.shortcuts import render
from .models import Years

# Create your views here.

def Years_Home(request):
    return render(request, "Years/Years_Home.html", {
        "years": Years.objects.all()
    })

def year(request, year_id):
    year = Years.objects.get(id=year_id)
    return render(request, "Years/Years_Layout.html", {
        "year": year
    })