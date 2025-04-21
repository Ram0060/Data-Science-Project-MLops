import os
import requests
from urllib.request import urlretrieve
from src.DataScience import logger
import zipfile
from src.DataScience.entity.config_entity import (DataIngestionconfig)

class Dataingestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} is downloaded, with following info: {headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists")
    
    def extract_zip_file(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)
            logger.info(f"Extracted all the files in {unzip_dir}")

    