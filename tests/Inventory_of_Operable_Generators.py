import os
import requests
import pandas as pd

def pipeline_eia_bronze(api_key, nome_base="Operable_Generators"):
    """
    Função principal que encapsula todo o processo.
    """
    
    # 1. Função interna para gerar os parâmetros
    def get_params():
        url = "https://api.eia.gov/v2/electricity/operating-generator-capacity/data/"
        params = {
            "api_key": api_key,
            "frequency": "monthly", 
            "offset": 0,
            "length": 5000
        }
        return url, params

    # 2. Função interna que consome a API (já usando a função anterior)
    def request_data():
        url, params = get_params()
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                resposta_json = response.json()
                return resposta_json.get("response", {}).get("data", [])
            else:
                print(f"Erro na API! Status code: {response.status_code}")
        except Exception as e:
            print(f"Erro de conexão: {e}")
        return []


    def salvar_dados_brutos():
        dados = request_data()
        
        if not dados:
            print("Nenhum dado coletado para salvar!")
            return None

        df_raw = pd.DataFrame(dados)
        os.makedirs("data", exist_ok=True)

        csv_way = os.path.join("data", f"{nome_base}.csv")
        parquet_way = os.path.join("data", f"{nome_base}.parquet")

        df_raw.to_csv(csv_way, index=False, encoding="utf-8")
        df_raw.to_parquet(parquet_way, index=False)
        
        print(f"Sucesso! Arquivos salvos em: {csv_way} e {parquet_way}")
        return df_raw

    return salvar_dados_brutos()