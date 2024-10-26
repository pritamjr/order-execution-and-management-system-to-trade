# src/api/auth.py
import requests
from config import settings


def get_access_token():
    url = f"{settings.API_URL}/public/auth"
    params = {
        'grant_type': 'client_credentials',
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['result']['access_token']
