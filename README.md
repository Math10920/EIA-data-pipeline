# EIA-Pipeline-International-Enercy

## O que é o EIA?



## Objetivo Geral do Projeto

Projetar e implementar uma plataforma de Engenharia de Dados End-to-End híbrida e resiliente, utilizando a API v2 da EIA como fonte de dados. O projeto adota uma estratégia de separação de ambientes — conduzindo a prototipagem, testes unitários e extração leve localmente via VS Code, e escalando o processamento distribuído, transformação e governança para a nuvem utilizando Databricks, PySpark e Delta Lake sob a Arquitetura Medallion (Bronze, Silver, Gold). Tudo isso é integrado por meio de Docker, orquestração automatizada e práticas de CI/CD via GitHub Actions.

---

## Objetivos Específicos do Projeto

1. Desenvolvimento Local, Testes e Ingestão Resiliente (Extract & Local Dev):
    * Desenvolver scripts modulares em Python no VS Code com tratamentos robustos de paginação iterativa (offset/length) e exceções HTTP.
    * Implementar testes unitários e validações locais para otimizar o ciclo de desenvolvimento sem incorrer em custos de computação em nuvem.
    * Empacotar a camada de ingestão utilizando Docker para garantir portabilidade e paridade de ambiente.

2. Governança e Persistência na Camada Bruta (Camada Bronze / Raw):
    * Ingerir os payloads JSON originais diretamente para o ecossistema em nuvem, armazenando-os de forma imutável para garantir linhagem de dados (data lineage) e capacidade total de reprocessamento (replay).

3. Processamento Distribuído, Limpeza e Validação (Camada Silver / Trusted):
    * Utilizar PySpark no Databricks para processar grandes volumes de dados de forma distribuída, realizando a normalização de JSONs aninhados, tipagem estrita de colunas e tratamento de valores nulos.
    * aplicar validações de qualidade de dados (Data Quality) para assegurar a integridade antes da promoção para tabelas estruturadas.

4. Modelagem Analítica e Performance Otimizada (Camada Gold / Processed):
    * Projetar e persistir tabelas analíticas agregadas utilizando o formato Delta Lake, aplicando otimizações de layout e compactação para garantir alta performance em consultas de BI e análises de transição energética.

5. Orquestração e Integração Contínua (Operations & CI/CD):
    * Orquestrar o fluxo ponta a ponta (Bronze $\rightarrow$ Silver $\rightarrow$ Gold) utilizando Databricks Workflows.Configurar um pipeline de CI/CD via GitHub Actions para automatizar a validação de código, testes e o deploy contínuo para o ambiente de produção.

---
## Quais dados foram escolhidos para este projeto?

1. Capacidade Instalada de Geração (Operating Generator Capacity):
    * O que abrange: Informações detalhadas sobre usinas de energia, divididas por fonte primária (solar, eólica, hidrelétrica, gás natural, carvão), capacidade nominal em megawatts (MW), localização geográfica (estado/condado) e cronogramas de novas entradas em operação ou aposentadorias.
    * Valor estratégico: Permite mapear a infraestrutura física de energia, analisar o ritmo de expansão de fontes renováveis e estudar a segurança de suprimento de uma região.

2. Geração Real e Vendas no Varejo (Electricity Generation & Retail Sales)
    * O que abrange: O volume real de eletricidade gerado ao longo do tempo e os dados de consumo segmentados por setores de mercado (residencial, comercial, industrial).
    * Valor estratégico: Fundamental para identificar padrões de consumo, sazonalidade climática (como picos de demanda no verão/inverno) e o comportamento da atividade econômica atrelada à indústria.

3. Preços e Tarifas de Energia (Electricity Prices)
    * O que abrange: Custos médios da eletricidade cobrados dos consumidores finais e preços no mercado atacadista.
    * Valor estratégico: Permite correlacionar o custo da energia com a competitividade industrial, inflação e impactos de choques de commodities fósseis.

4. Transição Energética e Sustentabilidade (Renewable Integration)
    * O que abrange: Métricas de descarbonização, participação relativa de fontes limpas na matriz e projeções de capacidade futura.
    * Valor estratégico: Altamente valorizado no mercado atual para análises ESG, relatórios de sustentabilidade corporativa e conformidade regulatória.
---

## Ferramentas e metodologias aplicadas no projeto

**IDE e SO:**
* ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
* ![WSL](https://img.shields.io/badge/WSL-0078D4?style=for-the-badge&logo=windows&logoColor=white)
* ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
* ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

**Linguagens:**
* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
* ![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)

**Versionamento dos projetos:**
* ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
* ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

**Armazenamento e Processamento de Big Data:**
* ![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
* ![Delta Lake](https://img.shields.io/badge/Delta_Lake-FF3621?style=for-the-badge&logo=deltalake&logoColor=white)

**Comtenrização:**
* ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
---

## Documentação Técnica
https://www.eia.gov/opendata/documentation.php

## API de Energia Internacional
https://www.eia.gov/opendata/browser/electricity/operating-generator-capacity
https://api.eia.gov/v2/electricity/electricity-power-operational-data/data/
https://api.eia.gov/v2/electricity/retail-sales/data/
https://api.eia.gov/v2/electricity/rto/region-data/data/



## Fluxograma do Projeto

1. **Configuração VENV no VS CODE pela SO do Ubuntu(WSL):**
2. **Versionamento no Github:**
3. **d**