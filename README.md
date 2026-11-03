# Relatório de Pedidos com Pagamento Recusado e Antifraude Legítimo

Projeto desenvolvido em **Python e PySpark** para processamento de dados de pedidos e pagamentos, aplicando regras de negócio para identificar pedidos com pagamento recusado, mas considerados legítimos pela análise antifraude.

## Objetivo

Construir um pipeline de Engenharia de Dados utilizando PySpark e Programação Orientada a Objetos (POO), capaz de processar arquivos CSV e JSON compactados, aplicar transformações e gerar um relatório final em formato Parquet.

## Regras de negócio

O relatório considera os seguintes critérios:

- Pagamentos com status de recusa (`STATUS = false`);
- Avaliação antifraude indicando operação legítima (`AVALIACAO_FRAUDE.fraude = false`);
- Pedidos realizados no ano de 2025;
- Agrupamento dos itens por pedido para calcular o valor total;
- Ordenação por UF, forma de pagamento e data do pedido.

## Tecnologias utilizadas

- Python 3.11
- PySpark
- Apache Spark
- Java 17
- Docker e Docker Compose
- Pytest
- Parquet
- Git e GitHub

## Arquitetura do projeto

```text
relatorio-pedidos-pyspark/
├── src/
│   └── relatorio_pedidos/
│       ├── config/
│       │   └── settings.py
│       ├── io/
│       │   └── data_reader.py
│       ├── business/
│       │   └── report_service.py
│       ├── pipeline/
│       │   └── pipeline.py
│       └── spark/
│           └── session.py
├── tests/
│   └── test_report_service.py
├── data/
├── output/
├── main.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Configuração do ambiente

### Pré-requisitos

- Git
- Docker Desktop

**Não é necessário instalar Python, Java, PySpark ou configurar Hadoop/Winutils localmente para executar o pipeline via Docker.**

### Clonar o repositório

```bash
git clone https://github.com/arthuroaraujo/relatorio-pedidos-pyspark.git
cd relatorio-pedidos-pyspark
```

### Preparar os dados

Disponibilize os datasets nas seguintes pastas:

```text
data/
├── pedidos/
└── pagamentos/
```

Os arquivos devem estar organizados conforme os caminhos definidos em `settings.py`.

## Execução via Docker

Com o Docker Desktop iniciado e os datasets disponíveis, execute:

```bash
docker compose up --build
```

O Docker será responsável por:

1. Construir a imagem com Python 3.11;
2. Instalar Java 17;
3. Instalar as dependências Python;
4. Configurar o ambiente de execução do Spark;
5. Executar o pipeline de processamento.

Os diretórios locais são compartilhados com o container por meio de volumes:

- `./data:/app/data`: disponibiliza os datasets;
- `./output:/app/output`: permite persistir os resultados localmente.

### Resultado

Após a execução, o relatório estará disponível em:

```text
output/relatorio_pedidos/
```

O resultado é gerado em formato Parquet.

## Execução dos testes

Para executar os testes unitários localmente, é necessário ter Python 3.11 e as dependências instaladas.

```bash
python -m pytest
```

## Resultado do processamento

Na execução realizada com os dados disponibilizados para o trabalho, foram obtidos os seguintes resultados:

| Etapa | Quantidade |
|---|---:|
| Pedidos lidos | 60.096 |
| Pagamentos lidos | 60.096 |
| Pagamentos recusados | 8.345 |
| Pagamentos recusados e legítimos | 2.747 |
| Pedidos após junção | 2.747 |
| Pedidos de 2025 | 1.473 |

## Estrutura do relatório final

O relatório Parquet contém as seguintes colunas:

| Coluna | Descrição |
|---|---|
| `id_pedido` | Identificador do pedido |
| `uf` | Unidade federativa do pedido |
| `forma_pagamento` | Forma de pagamento utilizada |
| `valor_total_pedido` | Valor total calculado do pedido |
| `data_pedido` | Data de criação do pedido |

## Conceitos aplicados

- Programação Orientada a Objetos;
- Injeção de dependências;
- Separação de responsabilidades;
- Centralização de configurações;
- Schemas explícitos;
- Transformações e agregações com PySpark;
- Tratamento de exceções;
- Logging;
- Testes unitários;
- Processamento distribuído;
- Persistência de dados em Parquet;
- Containerização com Docker.

## Autor

**Arthur Araújo**

GitHub: [arthuroaraujo](https://github.com/arthuroaraujo)

Repositório: [relatorio-pedidos-pyspark](https://github.com/arthuroaraujo/relatorio-pedidos-pyspark)
