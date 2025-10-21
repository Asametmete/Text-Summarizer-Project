import requests
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionEntity
import zipfile


class DataIngestion:
    
    def __init__(self, config:DataIngestionEntity):
        self.config = config
    
    def get_data_from_github(self):

        r = requests.get(self.config.source_url)

        with open(self.config.file_path_unzip_dataset, "wb") as file:
            file.write(r.content)

        logger.info(f"Dataset downloaded to {self.config.local_data_dir}")
        

    def unzip_data(self):
        
        with zipfile.ZipFile(self.config.file_path_unzip_dataset, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)