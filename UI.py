# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:00:45 2021

@author: Eric
"""

import tkinter as tk
# from backup.py import start_backup

# function to change the status text
# def update_status_text():
#     if activate_button.config('text')[-1] == 'Start Program':
#         activate_button.config(text='Stop Program')
#     else:
#         activate_button.config(text='Start Program')

def toggle():
    '''
    use
    t_btn.config('text')[-1]
    to get the present state of the toggle button
    '''
    if activate_button.config('text')[-1] == 'Start Program':
        activate_button.config(text='Stop Program')
        status_text.delete('0.6')
        status_text.insert(tk.END, 'Running')
    else:
        activate_button.config(text='Start Program')
        status_text.delete('0.6')
        status_text.insert(tk.END, 'Stopped')

# create the window, text and button widgets
window = tk.Tk()
status_text = tk.Text(window)

activate_button = tk.Button(window, text='Start Program',
                            command = toggle)

close_button = tk.Button(window, text = 'Exit', command = window.destroy)

# status text
running_text = 'Running'
stopped_text = 'Stopped'

# pack the widets
status_text.pack()  
activate_button.pack()
close_button.pack()

# insert the text into the
status_text.insert(tk.END, 'Stopped')

#def backup_call_back():

window.mainloop()
