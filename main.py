from src.textSummarizer.pipeline.stage_01_data_Ingestion import DataIngestionPipeline
from src.textSummarizer.pipeline.stage_02_data_Processing import DataProcessingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME_01 = "Data Ingestion"

try:
    logger.info(f"Stage {STAGE_NAME_01} started")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"Stage {STAGE_NAME_01} completed!")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME_02 = "Data Processing"

try:
      logger.info(f"Stage {STAGE_NAME_02} started")
      data_processing = DataProcessingPipeline()
      data_processing.main()
      logger.info(f"Stage {STAGE_NAME_02} completed!")
except Exception as e:
      logger.exception(e)
      raise e