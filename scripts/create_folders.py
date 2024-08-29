import os
from shutil import copy, move
from pathlib import Path

def create_folders(list_of_sim_folders,root_folder_path):
    """
    Makes the folders in a given path with given names. 

    Parameters
    ----------
    list_of_sim_folders: list of strings
        List specifying the names of the folders that we want to create. 
    root_folder_path: Pathlib.Path
        Path of the root folder where the other simulation folders will be made. 
    """
    for i in list_of_sim_folders:
        folder_path = Path(root_folder_path + f'/{i}/simulation/postProc')
        folder_path.mkdir(parents=True,exist_ok=True)