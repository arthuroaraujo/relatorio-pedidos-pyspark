from dataclasses import dataclass
from pathlib import Path

@dataclass
class Settings:
    app_name: str = "RelatorioPedidos"
    spark_master: str = "local[*]"
    pedidos_path: str = "data/pedidos"
    pagamentos_path: str = "data/pagamentos"
    output_path: str = "output/relatorio_pedidos"
    ano_referencia: int = 2025

    def validate_inputs(self) -> None:
        for path in (self.pedidos_path, self.pagamentos_path):
            if not Path(path).exists():
                raise FileNotFoundError(
                    f"Diretorio de dados nao encontrado: {path}. "
                    "Veja o README para baixar os datasets."
                )
