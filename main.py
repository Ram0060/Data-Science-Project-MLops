from src.DataScience import logger
from src.DataScience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DataScience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.DataScience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DataScience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>stage{STAGE_NAME} started<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>stage{STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>>stage{STAGE_NAME} started<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>>stage{STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>>>stage{STAGE_NAME} started<<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.initate_data_transformation()
    logger.info(f">>>>>>>stage{STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>>>stage{STAGE_NAME} started<<<<<<")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.initiate_model_trainer()
    logger.info(f">>>>>>>stage{STAGE_NAME} completed<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e