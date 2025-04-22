import os
import yaml
from src.DataScience import logger
import json 
import joblib 
import pickle
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError



@ensure_annotations
def read_yaml(path_to_ymal) -> ConfigBox:
    try:
        with open(path_to_ymal) as ymal_file:
            content = yaml.safe_load(ymal_file)
            logger.info(f"ymal file:{path_to_ymal} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:str) -> ConfigBox:
    with open(path, 'r') as f:
        content = json.load(f)
        logger.info(f"json file loaded at: {path}")
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(path:Path, data: Any):
    joblib.dump(value = data, filename=path)
    logger.info(f"data saved at: {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    data = joblib.load(path)
    logger.info(f"data loaded at: {path}")
    return data