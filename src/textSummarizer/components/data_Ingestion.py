import requests
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionEntity
import zipfile


class DataIngestion:
    
    def get_data_from_kaggle(self, data_Ingestion_entity: DataIngestionEntity):

        r = requests.get(data_Ingestion_entity.source_url)

        with open(data_Ingestion_entity.file_path_unzip_dataset, "wb") as file:
            file.write(r.content)

        logger.info(f"Dataset downloaded to {data_Ingestion_entity.local_data_dir}")
        

    def unzip_data(self,data_Ingestion_entity: DataIngestionEntity):
        
        with zipfile.ZipFile(data_Ingestion_entity.file_path_unzip_dataset, "r") as zip_ref:
            zip_ref.extractall(data_Ingestion_entity.unzip_dir)