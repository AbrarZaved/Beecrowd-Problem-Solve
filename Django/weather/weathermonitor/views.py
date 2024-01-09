from django.shortcuts import render
from django.http import HttpResponse

def home(request):
<<<<<<< HEAD
    import json
    import requests
    api_request=requests.get("https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=d5914fd897744f00add89bf52dbccd4c&include=minutely")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    
    return render(request,'home.html',{})
def about(request):
    return render(request,'about.html',{})
=======
    return render(request,'home.html',{})
>>>>>>> 049d486318770b0a0febe5699e65ef117c930f2c
