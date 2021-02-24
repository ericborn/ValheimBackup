# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:00:45 2021

@author: Eric
"""

import tkinter as tk
# import os
# import shutil
#from time import sleep
#import backup as bk

# Global running flag
running = False  

# backup execution
def backup():
    if running:  # Only do this if the Stop button has not been clicked
        print('hello')
    # After 1 second, call scanning again (create a recursive loop)
    window.after(1000, backup)

# start backup
def start_backup():
    """Enable scanning by setting the global flag to True."""
    global running
    #if running == False:
    print(running)
    running = True
    print(running)
    backup()
        
# stop backup
def stop_backup():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False

# !!! WONT KICK OFF start_backup ON FIRST CLICK, ONLY SECOND!!!
def toggle_button():
    '''
    function to start/stop the backup and toggle button/status text
    '''
    global running
    if running == False:
    #if activate_button.config('text')[-1] == 'Start Program':
        #running = True
        #activate_button.config(text='Stop Program')
        activate_button.config(text='Stop Program', command=start_backup)
        #activate_button.config(text='Stop Program', command=start_backup)
        status_text.delete(1.0, tk.END)
        status_text.insert(tk.END, 'Running')
        #print('started')
        #window.after(10000, delayed)
        print("running")
        
    else:
        #activate_button.config(text='Start Program')
        activate_button.config(text='Start Program', command=stop_backup)
        status_text.delete(1.0, tk.END)
        status_text.insert(tk.END, 'Stopped')
        #print('stopped')
        #return(False)
        print("Stopped")
        #running = False

# create the window, text and button widgets
window = tk.Tk()
status_text = tk.Text(window)

# grid setup
app = tk.Frame(window)
app.grid()

# activate button to start/stop the backups
activate_button = tk.Button(window, text='Start Program',
                            command = toggle_button)

# start button
start_button = tk.Button(window, text='Start Program', command = start_backup)

# stop button
stop_button = tk.Button(window, text='Stop Program', command = stop_backup)

# close button to exit the program gracefully
close_button = tk.Button(window, text = 'Exit', command = window.destroy)

# pack the text and button widets
#status_text.pack()
#activate_button.pack()
#close_button.pack()

# grid layout
status_text.grid()
activate_button.grid()
start_button.grid()
stop_button.grid()
close_button.grid()

# insert the default text into the widget
status_text.insert(tk.END, 'Stopped')

#window.after(1000, scanning)  # After 1 second, call scanning

# call the tk function to draw the window
window.mainloop()