from django.shortcuts import render,HttpResponse
import requests
import json
import logging


# Create your views here.
from requests import request


def home(request):
    news_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&apiKey=2906b7de24d84d6386b34fc7970f77bc")
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})


def business(request):
    news_api_request = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=2906b7de24d84d6386b34fc7970f77bc")
    api = json.loads(news_api_request.content)
    return render(request, 'business.html', {'api': api})


def terrorism(request):
    news_api_request = requests.get(
        "https://newsapi.org/v2/everything?q=terrorism&apiKey=2906b7de24d84d6386b34fc7970f77bc")
    api = json.loads(news_api_request.content)
    return render(request, 'terrorism.html', {'api': api})


def geopolitics(request):
    news_api_request = requests.get(
        "https://newsapi.org/v2/everything?q=geopolitics&apiKey=2906b7de24d84d6386b34fc7970f77bc")
    api = json.loads(news_api_request.content)
    return render(request, "geopolitics.html", {"api": api})


def crime(request):
    news_api_request = requests.get(
        " https://newsapi.org/v2/everything?q=crime&apiKey=2906b7de24d84d6386b34fc7970f77bc")
    api = json.loads(news_api_request.content)
    return render(request, "crime.html", {"api": api})


def search(request):
    search_term = request.GET['search']
    url = f'https://newsapi.org/v2/everything?q={search_term}&apiKey=2906b7de24d84d6386b34fc7970f77bc'
    data = requests.get(url)
    response = data.json()
    articles = response ['articles']
    context = {'articles': articles}
    return render(request, "search.html", context)


def CNN(request):
    return render(request, 'CNN.html')

def Bloomberg(request):
    return render(request, 'Bloomberg.html')

def ANI(request):
    return render(request, 'ANI.html')

def AiJazeera(request):
    return render(request, 'Aijazeera.html')

def SCMP(request):
    return render(request, 'SCMP.html')


logger = logging.getLogger(__name__)

from django.http import HttpResponse
