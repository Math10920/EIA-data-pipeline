import os
from dotenv import load_dotenv
import pandas as pd
import requests

load_dotenv()
API_KEY = os.getenv("EIA_API")

url = "https://api.eia.gov/v2/electricity/operating-generator-capacity/data/"
params = {"api_key": API_KEY, "frequency": "monthly", "offset": 0, "length": 5}

response = requests.get(url, params=params)

if response.status_code == 200:
  dados = response.json()

  # O pulo do gato: acessamos o nível correto do JSON onde estão as linhas dos dados
  # Geralmente na API v2 da EIA a estrutura é dados['response']['data']
  lista_registros = dados.get("response", {}).get("data", [])

  if lista_registros:
    # Agora criamos o DataFrame a partir da lista de dicionários correta
    df = pd.DataFrame(lista_registros)
    print("DataFrame criado com sucesso!")
    print(df.head())
  else:
    print("Aviso: A requisição retornou vazia na chave de dados.")
else:
  print(f"Erro na requisição: {response.status_code}")
  print(response.text)