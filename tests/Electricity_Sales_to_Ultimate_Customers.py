import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Ajustado para o nome padrão da chave no seu .env
API_KEY = os.getenv("EIA_API")

# URL correta da API v2 (sem 'browser' e terminando com '/data/')
url = "https://api.eia.gov/v2/electricity/retail-sales/data/"

params = {"api_key": API_KEY, 
          "frequency": "monthly", 
          "offset": 0, 
          "length": 5000
          }

print("Enviando requisição para a EIA...")
response = requests.get(url, params=params)

# Verifica se a requisição foi bem-sucedida (Status 200)
if response.status_code == 200:
  print("Status:", response.status_code)
  print("Tipo da resposta:", type(response))

  try:
    dados_json = response.json()
    
    registros = dados_json.get("response", {}).get("data", [])
    print(f"Total de registros obtidos nesta página: {len(registros)}")

  except requests.exceptions.JSONDecodeError:
    print("Erro: A resposta não veio em formato JSON válido.")
    print("Conteúdo recebido:", response.text[:500])

else:
  print(f"Erro na requisição! Status Code: {response.status_code}")
  print("Detalhes do erro:", response.text)