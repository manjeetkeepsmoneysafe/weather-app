from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from app.models import Data, User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
import json

# Create your views here.

@login_required
def save(request):
    data = json.loads(request.body)
    user = User.objects.filter(username = request.user).first().data.create(weatherInfo = data)
    user.save()
    return JsonResponse({
        "message": "Goooddd"
    })

@login_required
def delete(request):
    data = json.loads(request.body)
    user = User.objects.filter(username = request.user).first().data.delete(weatherInfo = data)
    user.save()
    return JsonResponse({
        "message": "Gooood"
    })


@login_required
def past(request):
    pass

def loginView(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, "app/login.html", {
                "message": "Wrong username or password"
            })
    else:
        return render(request, "app/login.html")

def createuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            myUser = User.objects.create_user(username=username, password=password)
            myUser.save()
            messages.info(request, "New user has been created!")
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/index.html")
    return render(request, "app/createNewUser.html")

@login_required
def logoutView(request):
    logout(request)
    return render(request, 'app/logout.html')
    

def index(request):
    if request.user.is_authenticated:
        cityData = Data.objects.values_list('city')
        countryData = Data.objects.values_list('country')

        d = list( dict.fromkeys(countryData) )
        uniqueCountryData = sorted(d, reverse=False)
        f = list ( dict.fromkeys(cityData) )
        uniqueCityData = sorted(f, reverse=False)

        def getCities(country):
            return Data.objects.filter(country=country)

        return render(request, "app/index.html",  {
            "city": getCities,
            "country": [i[0] for i in uniqueCountryData],
        })
    else:
        return redirect('login')


@login_required
def weather(request):
    if request.method == "GET":
        longtitude = request.GET.get("long")
        latitude = request.GET.get("lat")

        return render(request, "app/weather.html", {
            "longitude": longtitude,
            "latitude": latitude,
        })
    else:
        pass

def countries(request):
    country = request.GET.get("country")
    if request.GET.get("city") is None:
        myData = Data.objects.filter(country=country)
        v = ",".join(i.city for i in myData)
        return JsonResponse(v, safe=False)
    else:
        city = request.GET.get("city")
        myData = Data.objects.filter(country=country, city=city)
        v, n = myData.first().long, myData.first().lati
        return JsonResponse((v, n), safe=False)