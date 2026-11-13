import os
from dotenv import load_dotenv
import pandas as pd
import requests
import json

load_dotenv()

API_KEY = os.getenv("EIA_API")


def params_user(api_key):

    url = "https://api.eia.gov/v2/electricity/operating-generator-capacity/data/"

    params = {
      "api_key": api_key,
      "frequency": "monthly", 
      "offset": 0,
      "length": 5000}

    if url and params is not None:
      return url, params

    return None


def dados(url, params):

    response = requests.get(url, params=params)

    if response.status_code == 200:
      dados = response.json()
      print(f"{response.status_code}")

      try:

        if isinstance(dados, dict) and dados["response"] is not None:
          data = dados.get("response", {}).get("data", [])
          print(json.dumps(data, indent=4, ensure_ascii=False))
          return data
        
        else:
          print(f"Dados não representa um ducionário: {type(dados)} \
                ou valor {None}")
      except Exception as e:
        print(f"Erro! {e}")
    else:
      print(f"Erro! {response.status_code}")

    return []



def raw_operating_generator_capacity(data, nome_base="Operable_Generators"):

  if not data:
    print(f"Nenhum dado coletado!")
    return None

  df_raw = pd.DataFrame(data)

  os.makedirs("data", exist_ok=True)

  csv_way = os.path.join("data", f"{nome_base}.csv")
  parquet_way = os.path.join("data", f"{nome_base}.parquet")

  df_raw.to_csv(csv_way, index=False, encoding="utf-8")
  df_raw.to_parquet(parquet_way, index=False)


url, params = params_user(API_KEY)
data = dados(url, params)
raw_data = raw_operating_generator_capacity(data, "Raw_Inventory_of_Operable_Generators")
