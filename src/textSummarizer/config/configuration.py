from src.textSummarizer.utils.common import read_Yaml_File, create_folder
from src.textSummarizer.constants import CONFIG_FILE_PATH
from src.textSummarizer.entity import DataIngestionEntity, DataProcessingEntity
from pathlib import Path

class ConfigurationManager:
    def __init__(self):
        self.config = read_Yaml_File(CONFIG_FILE_PATH)

    def get_data_Ingestion(self) -> DataIngestionEntity:
        data_Ingestion = DataIngestionEntity(Path(self.config["DataIngestion"]["root_dir"]), 
                                       self.config["DataIngestion"]["source_url"], 
                                       Path(self.config["DataIngestion"]["local_data_dir"]),
                                       Path(self.config["DataIngestion"]["file_path_unzip_dataset"]), 
                                       Path(self.config["DataIngestion"]["unziped_dir"]))
        create_folder(data_Ingestion.root_dir)
        return data_Ingestion
    
    def get_data_Processing(self) -> DataProcessingEntity:
        data_Processing = DataProcessingEntity(Path(self.config["DataProcessing"]["root_dir"]),
                                            Path(self.config["DataProcessing"]["raw_train_data_dir"]),
                                            Path(self.config["DataProcessing"]["raw_test_data_dir"]),
                                            Path(self.config["DataProcessing"]["raw_validation_data_dir"]),
                                            Path(self.config["DataProcessing"]["train_dir"]),
                                            Path(self.config["DataProcessing"]["test_dir"]), 
                                            Path(self.config["DataProcessing"]["validation_dir"]))
        create_folder(data_Processing.root_dir)
        return data_Processing        