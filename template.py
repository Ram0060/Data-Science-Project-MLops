import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')                # Set up logging configuration

project_name = "DataScience"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componets/__init__.py",
    f"src/{project_name}/utiles/__init__.py",
    f"src/{project_name}/utiles/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"

]


for filepath in list_of_files:                                                           # loop through each file path in the list
    filepath = Path(filepath)                                                            # convert the string path to a Path object
    filedir, filename = os.path.split(filepath)                                         # split the path into directory and file name

    if filedir != "":                                                                       # if there's a directory in the path
        os.makedirs(filedir, exist_ok=True)                                          # create the directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for filename: {filename}")                      # log directory creation

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):              # if file doesn't exist or is empty
        with open(filepath, 'w') as f:                                                  # create an empty file
            pass                                                                         # do nothing, just create the file
        logging.info(f"creating file: {filepath}")                                          # log file creation
    else:
        logging.info(f"file already exists: {filepath}")                                    # log that file already exists
