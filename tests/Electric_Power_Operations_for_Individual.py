import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_EIA")

def user_config(api_key):

    if api_key is not None:
        
        url = "https://api.eia.gov/v2/electricity/facility-fuel/data/"

        params = {
            "api_key": api_key,
            "frequency": "monthly",
            "offset": 0,
            "length": 5000,
        }

        print(f"usuário existe!")
        return url, params

    print(f"Usuário não existe")
    return None

def request_api(url, params):

    if url and params is not None:

        print(f"Uniciando coleta de dados!")
        response = requests.get(url, params=params)

        try:
        
            if response.status_code == 200:

                data_dict = response.json()
                data = data_dict.get("response", {}).get("data", {})               
                print(f"Dados coletados!")
                return data

            return print(f"Error response: {response.status_code}")

        except requests.exceptions.JSONDecodeError as e:
            return print(f"Error Exception: {e}")

    return None

url, params = user_config(API_KEY)

df = request_api(url, params)

print(df)