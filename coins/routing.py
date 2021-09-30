from django.urls import path
from .consumers import CoinsComsumers

ws_urlpatterns = [
    path('', CoinsComsumers.as_asgi()),
]