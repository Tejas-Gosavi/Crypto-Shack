from django.shortcuts import render
from .models import Coin
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def index(request):
    coins = Coin.objects.only('name')
    context = {
        'coinsName': coins
    }
    return render(request, "index.html")