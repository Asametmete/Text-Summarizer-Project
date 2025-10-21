from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_Processing import DataProcessing

class DataProcessingPipeline:
    def __init__(self):
        pass
    
    def main():
        config = ConfigurationManager()
        data_Processing_Entity = config.get_data_Processing()
        data_Processing = DataProcessing(config= data_Processing_Entity)
        dataset = data_Processing.get_csv_file(data_Processing_Entity.raw_train_data_dir)
        processed = dataset.map(data_Processing.preprocessing,batched=True,batch_size=1024)
        dataset_test = data_Processing.get_csv_file(data_Processing_Entity.raw_test_data_dir)
        processed_test = dataset_test.map(data_Processing.preprocessing,batched=True,batch_size=1024)
        dataset_validation = data_Processing.get_csv_file(data_Processing_Entity.raw_validation_data_dir)
        processed_validation = dataset_validation.map(data_Processing.preprocessing,batched=True,batch_size=1024)
        data_Processing.save(processed,processed_validation,processed_test)