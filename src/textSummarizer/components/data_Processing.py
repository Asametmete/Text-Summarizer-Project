from pathlib import Path
from transformers import T5Tokenizer
from src.textSummarizer.entity import DataProcessingEntity
from datasets import Dataset
from datasets import load_dataset
from src.textSummarizer.logging import logger


class DataProcessing:

    def __init__(self, config: DataProcessingEntity):
        self.config = config

    def get_csv_file(self, file_path: Path):
        dataset = load_dataset('csv', data_files=file_path.absolute().as_posix())
        return dataset
    
    def preprocessing(self, dataset: Dataset):
        model_name = "t5-base"
        tokenizer = T5Tokenizer.from_pretrained(model_name)

        inputs = dataset["article"]
        targets = dataset["highlights"]

        model_inputs = tokenizer(
            inputs,
            max_length=512,
            truncation=True,
            padding="max_length"
        )

        with tokenizer.as_target_tokenizer():
            labels = tokenizer(
                targets,
                max_length=128,
                truncation=True,
                padding="max_length"
            )

        model_inputs["labels"] = labels["input_ids"]

        return model_inputs
    
    def save(self, train_dataset: Dataset, val_dataset: Dataset, test_dataset: Dataset):
        
        train_dataset.save_to_disk(self.config.train_dir)
        val_dataset.save_to_disk(self.config.validation_dir)
        test_dataset.save_to_disk(self.config.test_dir)

        logger.info("Processed data saved")