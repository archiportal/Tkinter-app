# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 23:49:04 2021

@author: ARCHISMAN ROY
"""

import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
# Creating tkinter window 
window = tk.Tk() 
window.title('Football selections') 
window.geometry('500x250')


# label text for title 
ttk.Label(window, text = "Football selections registration", 
		background = 'black', foreground ="yellow", 
		font = ("Times New Roman", 15)).grid(row = 0, column = 1) 

# label 
ttk.Label(window, text = "Select the position you play:", 
		font = ("Times New Roman", 10)).grid(column = 0, 
		row = 5, padx = 10, pady = 25) 

# Combobox creation 
n = tk.StringVar() 
choice = ttk.Combobox(window, width = 27, textvariable = n) 

# Adding combobox drop down list 
choice['values'] = ('Striker', 
						'Second striker', 
						'Left winger',
                        'Right winger',
                        'Attacking midfielder',
                        'Center midfielder',
                        'Defensive midfielder',
                        'Right back',
                        'Left back',
                        'Center back',
                        'Goalkeeper') 

choice.grid(column = 1, row = 5) 
choice.current() 

ttk.Label(window, text = "How many hours do you practice every week?",  
		font = ("Times New Roman", 15)).grid(row = 29, column = 0)
rad1=Radiobutton(window,text="2-6",value=1)
rad2=Radiobutton(window,text="7-10",value=2)
rad3=Radiobutton(window,text="More than 10",value=3)
rad1.grid(column=0,row=30)
rad2.grid(column=1,row=30)
rad3.grid(column=2,row=30)
#message box



def clicked():
	messagebox.showinfo('Rules','Rules will show here')
bt=Button(window,text="Rules",command=clicked)
bt.grid(row=35,column=1)

#checkbutton widget
ttk.Label(window, text = "Check this box if you want to join us for weekly practice sessions.",  
		font = ("Times New Roman", 15)).grid(row = 36, column = 0)
chk_state=BooleanVar() #variable of type BooleanVar
chk_state.set (True) # checked by default
chk=Checkbutton(window,text='I agree',var=chk_state) #passing the
#chk_state to the Checkbutton class to set the check state
chk.grid(column=0,row=37)

#entry field

tk.Label(window, text="Enter your email address:").grid(row=38)


e1 = tk.Entry(window)


e1.grid(row=39, column=0)

window.mainloop()
