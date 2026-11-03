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
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Funcionamento do pipeline

1. Inicialização da sessão Spark;
2. Leitura dos pedidos e pagamentos utilizando schemas explícitos;
3. Conversão e tratamento dos dados;
4. Agrupamento dos itens e cálculo do valor total dos pedidos;
5. Filtragem dos pagamentos recusados e considerados legítimos pela análise antifraude;
6. Junção entre pedidos e pagamentos;
7. Filtragem dos pedidos realizados em 2025;
8. Seleção das colunas finais e ordenação;
9. Escrita do relatório em formato Parquet.

## Configuração do ambiente

### Pré-requisitos

- Python 3.11
- Java 17
- Git

### Instalação

Clone o repositório:

```bash
git clone https://github.com/arthuroaraujo/relatorio-pedidos-pyspark.git
```

Entre na pasta:

```bash
cd relatorio-pedidos-pyspark
```

Crie o ambiente virtual:

```bash
py -3.11 -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Configuração adicional para Windows

Em algumas instalações do PySpark no Windows, é necessário configurar os binários nativos do Hadoop para que o Apache Spark funcione corretamente.

1. Disponibilize os arquivos `winutils.exe` e `hadoop.dll` compatíveis com a versão do Hadoop utilizada pelo PySpark.
2. Organize os arquivos na seguinte estrutura:

```text
C:\hadoop\
└── bin\
    ├── winutils.exe
    └── hadoop.dll
```

3. Configure as variáveis de ambiente no PowerShell:

```powershell
$env:HADOOP_HOME = "C:\hadoop"
$env:PATH += ";C:\hadoop\bin"
```

Essas configurações são válidas para a sessão atual do terminal. Caso necessário, configure as variáveis permanentemente no Windows.

> **Observação:** os binários nativos do Hadoop devem ser compatíveis com a versão utilizada pelo PySpark. A ausência ou incompatibilidade desses arquivos pode causar erros durante a execução do Spark no Windows.

Em ambientes Linux ou macOS, essa configuração específica de `winutils.exe` não é necessária.

## Execução

Com o ambiente configurado e os arquivos de entrada disponíveis nos caminhos definidos em `settings.py`, execute:

```bash
python main.py
```

O pipeline realizará o processamento dos dados e salvará o resultado no diretório:

```text
output/relatorio_pedidos/
```

O resultado é gerado em formato Parquet.

## Testes

Para executar os testes unitários:

```bash
python -m pytest
```

Os testes verificam a lógica de negócio implementada no processamento dos pedidos e pagamentos.

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
- Persistência de dados em Parquet.

## Autor

**Arthur Araújo**

Desenvolvedor de Software | Data Engineering

GitHub: [arthuroaraujo](https://github.com/arthuroaraujo)

Repositório: [relatorio-pedidos-pyspark](https://github.com/arthuroaraujo/relatorio-pedidos-pyspark)
