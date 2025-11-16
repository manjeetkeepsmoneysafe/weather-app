from django.shortcuts import render
from app.models import Data
from django.http import JsonResponse, HttpResponse

# Create your views here.
def index(request):
    cityData = Data.objects.values_list('city')
    countryData = Data.objects.values_list('country')

    d = list( dict.fromkeys(countryData) )
    uniqueCountryData = sorted(d, reverse=False)
    f = list ( dict.fromkeys(cityData) )
    uniqueCityData = sorted(f, reverse=False)

    def getCities(country):
        return Data.objects.filter(country=country)
        

    return render(request, "app/index.html", {
        "city": getCities,
        "country": [i[0] for i in uniqueCountryData],
    })


def weather(request):
    longtitude = request.GET.get("long")
    latitude = request.GET.get("lat")

    return render(request, "app/weather.html", {
        "longitude": longtitude,
        "latitude": latitude,
    })

def countries(request):
    country = request.GET.get("country")
    if request.GET.get("city") is None:
        myData = Data.objects.filter(country=country)
        v = ",".join(i.city for i in myData)
        print("Hello im here")
        return JsonResponse(v, safe=False)
    else:
        city = request.GET.get("city")
        myData = Data.objects.filter(country=country, city=city)
        v, n = myData.first().long, myData.first().lati
        return JsonResponse((v, n), safe=False)