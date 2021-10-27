
from django.shortcuts import render

# Create your views here

def home(request):
    import requests
    import json

    news_api_request = requests.get("https://newsapi.org/v2/everything?domains=wsj.com&apiKey=cac2a1dd412a400481c2d161d62377c5")
    api = json.loads(news_api_request.content)

    return render(request, 'home.html', {'api' : api})
    