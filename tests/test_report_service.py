from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType, BooleanType
from relatorio_pedidos.business.report_service import ReportService

def test_report_filters_refused_legitimate_payment():
    spark = (SparkSession.builder.master("local[1]")
             .appName("test-report-service").getOrCreate())
    pedidos_schema = StructType([
        StructField("ID_PEDIDO", StringType(), False),
        StructField("PRODUTO", StringType(), True),
        StructField("VALOR_UNITARIO", DoubleType(), True),
        StructField("QUANTIDADE", LongType(), True),
        StructField("DATA_CRIACAO", StringType(), True),
        StructField("UF", StringType(), True),
        StructField("ID_CLIENTE", StringType(), True),
    ])
    pagamentos_schema = StructType([
        StructField("ID_PEDIDO", StringType(), False),
        StructField("FORMA_PAGAMENTO", StringType(), True),
        StructField("VALOR_PAGAMENTO", DoubleType(), True),
        StructField("STATUS", BooleanType(), True),
        StructField("DATA_PROCESSAMENTO", StringType(), True),
        StructField("AVALIACAO_FRAUDE", StructType([
            StructField("fraude", BooleanType(), True),
            StructField("score", DoubleType(), True),
        ]), True),
    ])
    pedidos = spark.createDataFrame([
        ("P1","TV",100.0,2,"2025-02-10 10:00:00","RJ","C1"),
        ("P2","PC",500.0,1,"2025-02-10 10:00:00","SP","C2"),
        ("P3","MOUSE",50.0,1,"2024-02-10 10:00:00","RJ","C3"),
    ], pedidos_schema)
    pagamentos = spark.createDataFrame([
        ("P1","PIX",200.0,False,"2025-02-10",(False,0.1)),
        ("P2","BOLETO",500.0,True,"2025-02-10",(False,0.1)),
        ("P3","PIX",50.0,False,"2024-02-10",(False,0.1)),
    ], pagamentos_schema)
    try:
        rows = ReportService().build_report(pedidos,pagamentos,2025).collect()
        assert len(rows) == 1
        assert rows[0]["id_pedido"] == "P1"
        assert rows[0]["valor_total_pedido"] == 200.0
        assert rows[0]["forma_pagamento"] == "PIX"
    finally:
        spark.stop()
