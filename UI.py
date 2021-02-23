# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:00:45 2021

@author: Eric
"""

import tkinter as tk
from backup.py import start_backup

# create the window, text and button widgets
window = tk.Tk()
#status_text = tk.Text(window)

#activate_button_text = ['Start Program','Stop Program']

activate_button = tk.Button(window, text='Start Program')
                            #command = start_backup)

#close_button = tk.Button(window, text = 'Exit', command = window.destroy)

# status text
running_text = 'Running'
stopped_text = 'Stopped'

# pack the widets
#status_text.pack()  
activate_button.pack()
#close_button.pack()

# insert the text into the
#status_text.insert(tk.END, running_text)

#def backup_call_back():

window.mainloop()
