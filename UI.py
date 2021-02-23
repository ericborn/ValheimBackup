# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:00:45 2021

@author: Eric
"""

import tkinter as tk
#from backup import start_backup

def toggle_program():
    '''
    function to enable the backup and toggle button/status text
    '''
    if activate_button.config('text')[-1] == 'Start Program':
        activate_button.config(text='Stop Program')
        status_text.delete(1.0, tk.END)
        status_text.insert(tk.END, 'Running')
        return(True)
    else:
        activate_button.config(text='Start Program')
        status_text.delete(1.0, tk.END)
        status_text.insert(tk.END, 'Stopped')
        return(False)

# create the window, text and button widgets
window = tk.Tk()
status_text = tk.Text(window)

# activate button to start/stop the backups
activate_button = tk.Button(window, text='Start Program',
                            command = toggle_program)

# close button to exit the program gracefully
close_button = tk.Button(window, text = 'Exit', command = window.destroy)

# status text
running_text = 'Running'
stopped_text = 'Stopped'

# pack the text and button widets
status_text.pack()  
activate_button.pack()
close_button.pack()

# insert the text into the
status_text.insert(tk.END, 'Stopped')

# call the tk function to draw the window
window.mainloop()