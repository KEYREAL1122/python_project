# api_service.py
import requests

BASE_URL = 'http://localhost:3000'

def get_all_users():
    response = requests.get(f'{BASE_URL}/users')
    return response.json()

# You can add similar functions for flights, airlines, etc.
