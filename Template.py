import os 
from pathlib import Path
import logging 


logging.basicConfig(level=logging.INFO,format="[%(asctime)s]:%(message)s:")

project_name="Heart Failure Prediction"

list_of_file=[
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.ymal",
    "params.ymal", 
    "schema.ymal", 
    "main.py", 
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for file_path in list_of_file: 
    file_path=Path(file_path) 

    filedir,filename=os.path.split(file_path)

    if filedir !="": 
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"create directory;{filedir} for the file {filename}")

    if(not os.path.exists(file_path)) or (os.path.getsize(file_path)==0): 
        with open(file_path,"w")as f: 
            pass 
            logging.info(f"create a empty file:{file_path}")

    else: 
        logging.info(f"{filename} is already exists")
        