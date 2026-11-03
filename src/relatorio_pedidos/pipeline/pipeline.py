import logging

class Pipeline:
    def __init__(self, reader, report_service, settings):
        self.reader = reader
        self.report_service = report_service
        self.settings = settings

    def execute(self):
        self.settings.validate_inputs()
        logging.info("Lendo pedidos")
        pedidos = self.reader.read_pedidos(self.settings.pedidos_path)
        logging.info("Lendo pagamentos")
        pagamentos = self.reader.read_pagamentos(self.settings.pagamentos_path)
        relatorio = self.report_service.build_report(
            pedidos, pagamentos, self.settings.ano_referencia
        )
        logging.info("Gravando Parquet em %s", self.settings.output_path)
        self.reader.write_parquet(relatorio, self.settings.output_path)
        logging.info("Pipeline finalizado")
