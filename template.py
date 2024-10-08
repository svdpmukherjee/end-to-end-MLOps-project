import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    # If path is Path("src/project/file.txt"), then path.parent would be Path("src/project"); If the directory already exists, the exist_ok=True parameter ensures no error is raised
    
    if not path.exists() or path.stat().st_size == 0: 
    # Checks if the file specified by path exists or any existing file size is 0 bytes
        
        path.write_text('')
        logging.info(f"Created/Updated empty file: {path}")
    else:
        logging.info(f"{path.name} already exists")
