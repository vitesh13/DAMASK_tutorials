import os
from shutil import copy, move
from pathlib import Path
from damask import Rotation
from damask import ConfigMaterial as cm

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
        folder_path = Path(root_folder_path,f'/{i}/simulation/postProc')
        folder_path.mkdir(parents=True,exist_ok=True)

def create_material_files(ori,list_of_sim_folders,jupyter_cwd,root_folder_path):
    """
    Creates material files as needed in different folders. 

    Parameters
    ----------
    ori: damask.Rotation
        orientations needed to be created. 
    list_of_sim_folders: list of strings
        List specifying the names of the folders that we want to create. 
    jupyter_cwd: pathlib.Path
        Path of the jupyter notebook.
    root_folder_path: Pathlib.Path
        Path of the root folder where the other simulation folders will be made. 
    """
    cm_initial = cm.load(Path(jupyter_cwd,'/example/material.yaml'))
    phase_entry = cm_initial['phase']
    homog_entry = cm_initial['homogenization']
    cm_new = cm().material_add(O=ori,phase='phase_A',homogenization='SX')
    cm_new['phase'] = phase_entry                            # we dont change the phase parameters, so we copy them from example file
    cm_new['homogenization'] = homog_entry                   # we dont change the homogenization parameters, so we copy them from example file 
    for i in list_of_sim_folders:
        cm_new.save(Path(root_folder_path,f'material_{i}.yaml'))

def create_load_files(ori,list_of_sim_folders,jupyter_cwd,root_folder_path):
    """
    Creates material files as needed in different folders. 

    Parameters
    ----------
    ori: damask.Rotation
        orientations needed to be created. 
    list_of_sim_folders: list of strings
        List specifying the names of the folders that we want to create. 
    jupyter_cwd: pathlib.Path
        Path of the jupyter notebook.
    root_folder_path: Pathlib.Path
        Path of the root folder where the other simulation folders will be made. 
    """
    cm_initial = cm.load(Path(jupyter_cwd,'/example/material.yaml'))
    phase_entry = cm_initial['phase']
    homog_entry = cm_initial['homogenization']
    cm_new = cm().material_add(O=ori,phase='phase_A',homogenization='SX')
    cm_new['phase'] = phase_entry                            # we dont change the phase parameters, so we copy them from example file
    cm_new['homogenization'] = homog_entry                   # we dont change the homogenization parameters, so we copy them from example file 
    for i in list_of_sim_folders:
        cm_new.save(Path(root_folder_path,f'material_{i}.yaml'))
    