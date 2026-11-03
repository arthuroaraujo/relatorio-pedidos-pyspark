
import logging

from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    sum as spark_sum,
    year,
    to_timestamp,
    to_date,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class ReportService:
    def build_report(
        self,
        pedidos: DataFrame,
        pagamentos: DataFrame,
        ano: int,
    ) -> DataFrame:
        try:
            logging.info("Total de pedidos: %s", pedidos.count())
            logging.info("Total de pagamentos: %s", pagamentos.count())

            logging.info("Schema pedidos:")
            pedidos.printSchema()

            logging.info("Schema pagamentos:")
            pagamentos.printSchema()

            logging.info("Amostra pagamentos:")
            pagamentos.show(5, truncate=False)

            logging.info("Convertendo data de criacao dos pedidos")
            pedidos = pedidos.withColumn(
                "DATA_CRIACAO",
                to_timestamp(col("DATA_CRIACAO")),
            )

            logging.info("Calculando valor total por pedido")
            pedidos_agg = pedidos.groupBy(
                "ID_PEDIDO",
                "UF",
                "DATA_CRIACAO",
            ).agg(
                spark_sum(
                    col("VALOR_UNITARIO") * col("QUANTIDADE")
                ).alias("VALOR_TOTAL_PEDIDO")
            )

            logging.info(
                "Filtrando pagamentos recusados e antifraude legitimos"
            )
            pagamentos_ok = pagamentos.filter(
                (col("STATUS") == False)
                & (col("AVALIACAO_FRAUDE.fraude") == False)
            )

            logging.info(
                "Pagamentos com STATUS false: %s",
                pagamentos.filter(col("STATUS") == False).count(),
            )

            logging.info(
                "Pagamentos recusados e antifraude legítimos: %s",
                pagamentos_ok.count(),
            )

            logging.info(
                "Pedidos agregados: %s",
                pedidos_agg.count(),
            )

            pedidos_join = pedidos_agg.join(
                pagamentos_ok,
                on="ID_PEDIDO",
                how="inner",
            )

            logging.info(
                "Pedidos após join: %s",
                pedidos_join.count(),
            )

            logging.info("Filtrando pedidos pelo ano: %s", ano)

            resultado = pedidos_join.filter(
                year(col("DATA_CRIACAO")) == ano
            )

            logging.info(
                "Pedidos após filtro de ano: %s",
                resultado.count(),
            )

            resultado = resultado.select(
                col("ID_PEDIDO").alias("id_pedido"),
                col("UF").alias("uf"),
                col("FORMA_PAGAMENTO").alias("forma_pagamento"),
                col("VALOR_TOTAL_PEDIDO").alias("valor_total_pedido"),
                to_date(col("DATA_CRIACAO")).alias("data_pedido"),
            ).orderBy(
                "uf",
                "forma_pagamento",
                "data_pedido",
            )

            logging.info("Relatorio pronto")

            return resultado

        except Exception:
            logging.exception("Erro na logica de negocio")
            raise
