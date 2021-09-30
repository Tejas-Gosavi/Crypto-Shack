import requests
from .models import Coin
from django.forms.models import model_to_dict
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from math import floor

channel_layer = get_channel_layer()

@shared_task
def get_coins_data():
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    data = response.json()
    coins = []

    for coin in data:
        coin_instance, created = Coin.objects.get_or_create(symbol=coin['symbol'].upper())
        
        coin_instance.name = coin['name']
        coin_instance.symbol = coin['symbol'].upper()
        coin_instance.rank = coin['market_cap_rank']
        coin_instance.image = coin['image']

        if coin_instance.price < coin['current_price']:
            current_price_state = "rise"
        elif coin_instance.price > coin['current_price']:
            current_price_state = "fall"
        else:
            current_price_state = "same"

        if coin['price_change_percentage_24h'] > 0:
            price_change_percentage_24h_state = "rise"
        else:
            price_change_percentage_24h_state = "fall"

        coin_instance.price = coin['current_price']
        coin_instance.price_change_percentage_24h = floor(coin['price_change_percentage_24h'] * 100)/100.0
        
        coin_instance.save()
        coin_dict = model_to_dict(coin_instance)
        coin_dict.update({'current_price_state': current_price_state, 'price_change_percentage_24h_state': price_change_percentage_24h_state})

        coins.append(coin_dict)

    async_to_sync(channel_layer.group_send)('coins', {'type': 'send_new_data', 'text': coins})