from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app/index.html")

def weather(request):
    longtitude = request.GET.get("long")
    latitude = request.GET.get("lat")

    return render(request, "app/weather.html", {
        "longitude": longtitude,
        "latitude": latitude,
    })
