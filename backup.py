# -*- coding: utf-8 -*-
"""
Eric Born

Script to auto backup
"""
import os
import shutil
from time import sleep
import tkinter

root_path = r'C:\Users\Eric\AppData\LocalLow\IronGate\Valheim'

back_path = r'C:\Users\Eric\AppData\LocalLow\IronGate\Valheim\backup'
#char_files = r'C:\Users\Eric\AppData\LocalLow\IronGate\Valheim\characters\\'
#world_files = r'C:\Users\Eric\AppData\LocalLow\IronGate\Valheim\worlds\\'

path_list = ['\\characters\\', '\\worlds\\']

# iterate 1-3 for the various backup versions
for increment in range(1,4):
    # create full path to the backup location
    full_back_path = back_path + '\\' + str(increment) + '\\'
    print(full_back_path)
    
    # iterate through the path list
    for paths in path_list:
        # create a list from the files in the path
        src_files = os.listdir(root_path + paths)
        #print(src_files)
        
        # iterate through the file list
        for file_name in src_files:
            # create the full filepath to the file
            full_file_name = os.path.join(root_path + paths, file_name)
            #print(full_file_name)
            
            # if the file is valid
            if os.path.isfile(full_file_name):
                # copy the file from the current location to the backup location
                shutil.copy(full_file_name, full_back_path)
                #print(full_file_name, full_back_path)
    
    # sleep for the 15 minutes until the game automatically saves itself
    sleep(900)