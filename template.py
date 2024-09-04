import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "house_price_prediction"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exceptions.py",
    f"src/{project_name}/constants.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "setup.py",
    "requirements.txt",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  
            logging.info(f"{filename} created!")  # Create an empty file

    else:
        logging.info(f"{filename} already exists!")