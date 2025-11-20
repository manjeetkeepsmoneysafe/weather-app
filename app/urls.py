from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("weather/", views.weather, name="weather"),
    path("countries/", views.countries, name='countries'),
    path("login/", views.loginView, name="login"),
    path("create/", views.createuser, name="create"),
    path("logout/", views.logoutView, name="logout"),
    path("save/", views.save, name="save"),
    path("past/", views.past, name="past")
]
