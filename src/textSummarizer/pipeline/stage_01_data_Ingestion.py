from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_Ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_Ingestion_Entity= config.get_data_Ingestion()
        dataIngestion = DataIngestion(config=data_Ingestion_Entity)
        dataIngestion.get_data_from_github()   
        dataIngestion.unzip_data()

