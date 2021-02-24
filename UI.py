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

running = True  # Global flag

def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        print('hello')

    # After 1 second, call scanning again (create a recursive loop)
    window.after(1000, scanning)
    
def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False


def toggle_program():
    '''
    function to enable the backup and toggle button/status text
    '''
    #main()
    if activate_button.config('text')[-1] == 'Start Program':
        activate_button.config(text='Stop Program', command=start)
        status_text.delete(1.0, tk.END)
        status_text.insert(tk.END, 'Running')
        #print('started')
        #window.after(10000, delayed)
        print(True)
        #return(True)
    else:
        activate_button.config(text='Start Program', command=stop)
        status_text.delete(1.0, tk.END)
        status_text.insert(tk.END, 'Stopped')
        #print('stopped')
        #return(False)
        print(False)



# create the window, text and button widgets
window = tk.Tk()
status_text = tk.Text(window)

# activate button to start/stop the backups
activate_button = tk.Button(window, text='Start Program',
                            command = toggle_program)

# start button
start_button = tk.Button(window, text='Start Program', command = start)

# stop button
stop_button = tk.Button(window, text='Start Program', command = stop)

# close button to exit the program gracefully
close_button = tk.Button(window, text = 'Exit', command = window.destroy)

# pack the text and button widets
status_text.pack()  
activate_button.pack()
close_button.pack()

# insert the default text into the widget
status_text.insert(tk.END, 'Stopped')

# call the tk function to draw the window
window.mainloop()