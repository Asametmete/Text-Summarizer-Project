from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_Ingestion import DataIngestion

try:
    config = ConfigurationManager()
    data_Ingestion_Entity= config.get_data_Ingestion()
    dataIngestion = DataIngestion()
    dataIngestion.get_data_from_kaggle(data_Ingestion_Entity)   
    dataIngestion.unzip_data(data_Ingestion_Entity)

except:
    logger.info("An exception occurred")