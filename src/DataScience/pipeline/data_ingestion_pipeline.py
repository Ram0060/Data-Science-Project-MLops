from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.componets.data_ingestion import Dataingestion
from src.DataScience import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        dataingestion = Dataingestion(config=data_ingestion_config)
        dataingestion.download_file()
        dataingestion.extract_zip_file()
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>stage{STAGE_NAME} started<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>stage{STAGE_NAME} completed<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


















    
