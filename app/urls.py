from django.contrib import admin
from django.urls import path
from app import views

app_name = 'main'

urlpatterns = [
    # path('', views.index, name="home"),    
    path('', views.WeatherApi.as_view(), name="weather_api"),
]
