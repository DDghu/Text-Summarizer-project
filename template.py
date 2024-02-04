import os
from pathlib import Path
import logging #for existing login we log them simultaneously

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


project_name="textSummarizer" #we can take it chicken disease classifier

list_of_files=[
    ".github/workflows/.gitkeep", #we keep yaml file but initially we create .gitkeep file ,if .gitkeep is not there then it doesn't reflect on github
    f"src/{project_name}/__init__.py", # this project is not present in py pi so we need to create this as a local package so we initialize the constructor file
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml" ,
    "app.py",
    "main.py",
    "Dockerfile",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",#before implementing the actual components I try to create notebook experiment in this
    "templates/index.html"  #cause we going to create a flask web app
]

for filepath in list_of_files:
    filepath=Path(filepath) # cause we give in the filepath forward slash but windows use backward slash so we use Path and fix this
    filedir,filename= os.path.split(filepath)

    if filedir!= "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # second logic defines if there is any folder with some content don't remove it
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")