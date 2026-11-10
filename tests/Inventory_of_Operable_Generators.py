import os
from dotenv import load_dotenv
import pandas as pd
import requests
import json

load_dotenv()

API_KEY = os.getenv("EIA_API")

url = "https://api.eia.gov/v2/electricity/operating-generator-capacity/data/"

params = {
  "api_key": API_KEY,
  "frequency": "monthly", 
  "offset": 0,
  "length": 5000}

response = requests.get(url, params=params)

if response.status_code == 200:
  dados = response.json()
  print(f"{response.status}")

  try:

    if isinstance(dados, dict) and dados["response"] is not None:
      lista_registro = dados.get("response", {}).get("data", [])
      print(json.dumps(lista_registro, indent=4, ensure_ascii=False))

    else:
      print(f"Dados não representa um ducionário: {type(dados)} \
            ou valor {None}")

  except Exception as e:
    print(f"Erro! {e}")

else:
  print(f"Erro! {response.status_code}")

