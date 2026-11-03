from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import (
    StructType, StructField, StringType, DoubleType, LongType, BooleanType
)

class DataReader:
    def __init__(self, spark: SparkSession):
        self.spark = spark
        # Schema alinhado aos nomes publicados nos datasets do professor.
        self.pedidos_schema = StructType([
            StructField("ID_PEDIDO", StringType(), False),
            StructField("PRODUTO", StringType(), True),
            StructField("VALOR_UNITARIO", DoubleType(), True),
            StructField("QUANTIDADE", LongType(), True),
            StructField("DATA_CRIACAO", StringType(), True),
            StructField("UF", StringType(), True),
            StructField("ID_CLIENTE", StringType(), True),
        ])
        self.pagamentos_schema = StructType([
            StructField("id_pedido", StringType(), False),
            StructField("forma_pagamento", StringType(), True),
            StructField("valor_pagamento", DoubleType(), True),
            StructField("status", BooleanType(), True),
            StructField("data_processamento", StringType(), True),
            StructField("avaliacao_fraude", StructType([
                StructField("fraude", BooleanType(), True),
                StructField("score", DoubleType(), True),
            ]), True),
        ])

    def read_pedidos(self, path: str) -> DataFrame:
        return (self.spark.read.schema(self.pedidos_schema)
                .option("header", True).option("sep", ";")
                .option("compression", "gzip").csv(path))

    def read_pagamentos(self, path: str) -> DataFrame:
        pagamentos = (
            self.spark.read
            .schema(self.pagamentos_schema)
            .option("compression", "gzip")
            .json(path)
        )

        return (
            pagamentos
            .withColumnRenamed("id_pedido", "ID_PEDIDO")
            .withColumnRenamed("forma_pagamento", "FORMA_PAGAMENTO")
            .withColumnRenamed("valor_pagamento", "VALOR_PAGAMENTO")
            .withColumnRenamed("status", "STATUS")
            .withColumnRenamed("data_processamento", "DATA_PROCESSAMENTO")
            .withColumnRenamed("avaliacao_fraude", "AVALIACAO_FRAUDE")
        )

    def write_parquet(self, df: DataFrame, path: str) -> None:
        df.write.mode("overwrite").parquet(path)
