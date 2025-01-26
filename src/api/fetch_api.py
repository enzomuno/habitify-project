import os
import requests
from src.utils import to_iso8601_21, to_iso8601_23


# Definir as datas para rodar o código (Sempre será a data que o código está rodando)
actual_date_23 = to_iso8601_23()
actual_date_21 = to_iso8601_21()

HABITIFY_API_KEY = os.getenv('HABITIFY_API_KEY')

base_url = 'https://api.habitify.me'




# Função principal para consuma da url base.
def fetch_api(endpoint, params=None):

    api_url = f'{base_url}/{endpoint}'
    headers = {'Authorization': API_KEY}

    try:
        response = requests.get(url=api_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o endpoint {endpoint}: {e}")
        return None




# Consumir o endpoint journal
def fetch_journal(target_date=actual_date_23):
    data = fetch_api(endpoint="journal", params={"target_date":target_date})['data']
    return data

# Consumir o endpoint habits
def fetch_habits():
    data = fetch_api(endpoint="habits")['data']
    return data

# Consumir o endpoint moods
def fetch_moods(target_date=actual_date_21):
    data = fetch_api(endpoint="moods", params={"target_date":target_date})['data']
    return data

# Consumir o endpoint areas
def fetch_areas():
    data = fetch_api(endpoint="areas")['data']
    return data
