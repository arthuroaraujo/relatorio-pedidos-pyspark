from relatorio_pedidos.config.settings import Settings
from relatorio_pedidos.spark.session import SparkSessionManager
from relatorio_pedidos.io.data_reader import DataReader
from relatorio_pedidos.business.report_service import ReportService
from relatorio_pedidos.pipeline.pipeline import Pipeline

def main():
    settings = Settings()
    spark_manager = SparkSessionManager(settings.app_name, settings.spark_master)
    spark = spark_manager.create_session()
    reader = DataReader(spark)
    service = ReportService()
    pipeline = Pipeline(reader, service, settings)
    try:
        pipeline.execute()
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
