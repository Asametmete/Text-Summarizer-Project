from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionEntity:
    root_dir: Path
    source_url: str
    local_data_dir:Path
    file_path_unzip_dataset:Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataProcessingEntity:
    root_dir: Path
    raw_train_data_dir:Path
    raw_test_data_dir:Path
    raw_validation_data_dir:Path
    train_dir: Path
    test_dir: Path
    validation_dir: Path