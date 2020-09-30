from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework import serializers
from rest_framework.views import APIView
import requests
import datetime

from app.isPrime import myFunction
from app.models import WeatherAudit
from app.serializer import WeatherAuditSerializer

# home-page Trial Page
def index(request):
    # temporary API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ffd3b26e4c82f9cb533cb4cd9e1f2c65'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() 
    # print(city_weather)
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    context = {'weather' : weather}
    return render(request, 'pages/index.html', context)



"""
Requirement 

    1. get any json output from https://openweathermap.org/api
    2. create Python api which send same json output if current date(day) is prime
    3. if current date(day) is not prime then api will send "Date is not prime so no date"
    4. Add audit data in database.

"""
class WeatherApi(APIView):
    # see audit data
    def get(self, request):
        # data = request.data
        obj = WeatherAudit.objects.all()
        result = WeatherAuditSerializer(obj, many=True)
        return Response(result.data)

    def post(self, request):
        now = datetime.datetime.now()
        # current day => now.day
        if myFunction.isPrime(now.day):
            # means prime
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ffd3b26e4c82f9cb533cb4cd9e1f2c65'
            city = 'Las Vegas'
            city_weather = requests.get(url.format(city)).json() 
            # print(city_weather)
            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }
            
            # save audit
            WeatherAudit.objects.create(
                city=weather['city'],
                temperature=weather['temperature'],
                description=weather['description'],
                icon=weather['icon']
            )
            # return same json
            return Response(weather)
        return Response("Date is not prime so no date")
