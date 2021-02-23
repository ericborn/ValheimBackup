# -*- coding: utf-8 -*-
"""
Eric Born

Script to auto backup
"""
import os

root_path = r'C:\Users\Eric\AppData\LocalLow\IronGate\Valheim'

back_path = r'C:\Users\Eric\AppData\LocalLow\IronGate\Valheim\backup\\'
char_files = r'C:\Users\Eric\AppData\LocalLow\IronGate\Valheim\characters\\'
world_files = r'C:\Users\Eric\AppData\LocalLow\IronGate\Valheim\worlds\\'

paths = [char_files, world_files]

test_path = ['\\characters\\', '\\worlds\\']

os.listdir(root_path + test_path[0])

for paths in test_path:
    src_files = os.listdir(paths)

    for files in 