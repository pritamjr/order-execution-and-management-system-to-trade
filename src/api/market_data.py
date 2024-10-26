# src/api/market_data.py
import requests
from config import settings

def get_orderbook(symbol):
    url = f"{settings.API_URL}/public/get_order_book?instrument_name={symbol}"
    response = requests.get(url)
    return response.json()

def get_positions(access_token):
    url = f"{settings.API_URL}/private/get_positions"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()
