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
      return url , params

    return None


def dataframe(url, params):

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



def df_pandas():
    
    url, params = params_user(API_KEY)

    if url and params is not None:
      data = dataframe(url, params)

      if data: 

        df_final = pd.DataFrame(data).reset_index()
        return df_final

      return print(f"Não há dados disponíveis no Dataframe!")

    return print(f"Não há url e/ou parametros definidos!")


df_final = df_pandas()

print(df_final)