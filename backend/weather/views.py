from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import urllib.request
import json


from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login


# Create your views here.


def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # print(city)

        api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                         city + '&units=metric&appid=740ce9b853f60791d00a2bf992253d13').read()
        api_url2 = json.loads(api_url)

        data = {
            "country": city,
            "weather_description": api_url2['weather'][0]['description'],
            "weather_temperature": api_url2['main']['temp'],
            "weather_pressure": api_url2['main']['pressure'],
            "weather_humidity": api_url2['main']['humidity'],
            "weather_icon": api_url2['weather'][0]['icon'],
        }

    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity": None,
            "weather_icon": None,
        }
    print(data['weather_icon'])
    return render(request, 'weather.html', {"city": city, "data": data})
