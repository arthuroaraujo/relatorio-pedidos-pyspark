# Relatorio de pedidos - PySpark

Projeto acadêmico de Data Engineering Programming.

## O que faz
- Lê pedidos CSV gzip e pagamentos JSON gzip com schemas explícitos.
- Seleciona pagamentos `STATUS=false` e `AVALIACAO_FRAUDE.fraude=false`.
- Calcula valor total dos itens por pedido.
- Filtra pedidos do ano de 2025.
- Ordena por UF, forma de pagamento e data.
- Grava o resultado em Parquet.

## Requisitos
- Windows 10/11
- Python 3.10 ou 3.11
- Java 17 (JDK)
- Git

## Preparar os dados (PowerShell na raiz do projeto)
```powershell
git clone https://github.com/infobarbosa/datasets-csv-pedidos.git temp-pedidos
git clone https://github.com/infobarbosa/dataset-json-pagamentos.git temp-pagamentos
New-Item -ItemType Directory -Force data\pedidos,data\pagamentos | Out-Null
Copy-Item temp-pedidos\data\pedidos\*.gz data\pedidos\
Copy-Item temp-pagamentos\data\pagamentos\*.gz data\pagamentos\
Remove-Item temp-pedidos,temp-pagamentos -Recurse -Force
```

## Instalar (PowerShell)
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

## Executar
```powershell
python main.py
```
Saída: `output\relatorio_pedidos` (Parquet).

## Testar
```powershell
pytest
```

## Observação de schema
Os schemas foram definidos explicitamente a partir dos nomes divulgados nos repositórios.
Se o CSV/JSON baixado tiver tipos ou nomes diferentes, ajuste `data_reader.py` antes da execução.
