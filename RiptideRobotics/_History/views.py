from django.shortcuts import render

# Create your views here.

def History_Home(request):
    return render(request, "History/_History_Home.html", {
        "histories": History.objects.all()
    })