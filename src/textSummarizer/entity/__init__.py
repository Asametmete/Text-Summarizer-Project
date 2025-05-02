from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionEntity:
    root_dir: Path
    source_url: str
    local_data_dir:Path
    file_path_unzip_dataset:Path
    unzip_dir: Path