import requests
import os
import json
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("EIA_API")

def api_conf(api_key):

    if api_key is not None:

        url = "https://api.eia.gov/v2/electricity/retail-sales/data/"

        params = {
            "api_key": api_key,
            "frequency": "monthly",
            "offset": 0,
            "length": 5000,
        }

        print(f"usuário permitido!")
        return url, params

    return print(f"Error: {None}")
    
def request_api(url, params):

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data_dict = response.json()
        print(f"Tipo de dados: {type(data_dict)}")

        try:
            data = data_dict.get("response", {}).get("data", {})
            data_json = json.dumps(data, indent=4, ensure_ascii=False)
            print(data_json)
            return data

        except requests.exceptions.JSONDecodeError as e:
            return print(f"Error message: {e}")

    else:
        return print(f"Status_code: {response.status_code} \
            \n Descrição do erro: {response.text}")

url, params = api_conf(API_KEY)

df = request_api(url, params)

print(df)