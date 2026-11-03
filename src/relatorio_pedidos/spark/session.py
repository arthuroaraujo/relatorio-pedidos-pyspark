from pyspark.sql import SparkSession

class SparkSessionManager:
    def __init__(self, app_name: str, master: str):
        self.app_name = app_name
        self.master = master

    def create_session(self) -> SparkSession:
        return (SparkSession.builder.appName(self.app_name)
                .master(self.master).getOrCreate())
