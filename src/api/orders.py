# src/api/orders.py
import requests
from config import settings

def place_order(access_token, symbol, order_type, amount, price):
    url = f"{settings.API_URL}/private/buy"
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        'instrument_name': symbol,
        'amount': amount,
        'type': order_type,
        'price': price
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def cancel_order(access_token, order_id):
    url = f"{settings.API_URL}/private/cancel"
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {'order_id': order_id}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def modify_order(access_token, order_id, new_price, new_amount):
    cancel_order(access_token, order_id)
    return place_order(access_token, 'BTC-PERPETUAL', 'limit', new_amount, new_price)
