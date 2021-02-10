# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:58:03 2021

@author: ARCHISMAN ROY
"""

from tkinter import *
window=Tk()
window.geometry("312x324")
window.title("Simple Calculator")

def b_click(i):
    global exp
    exp = exp +str(i)
    input_text.set(exp)
def b_clear():
    global exp
    exp = ""
    input_text.set("")
def b_equal():
    global exp
    result = str(eval(expression))
    input_text.set(result)
    exp = ""
exp = ""
input_text=StringVar()

input_frame = Frame(window,width=312, height=50, bd=0)
input_frame.pack(side=TOP)

input_field=Entry(input_frame, font=('arial',18,'bold'),textvariable=input_text,width=50,bd=0)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

button_frame=Frame(window,width=312,height=272.5,bg="grey")
button_frame.pack

clear=Button(button_frame,text="C",fg="black",width=32,height=3,bd=2,cursor="hand2",command=lambda:b_clear())
divide=Button(button_frame,text="/",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click('/'))
seven=Button(button_frame,text="7",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click(7))
eight=Button(button_frame,text="8",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click(8))
nine=Button(button_frame,text="9",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click(9))
multiply=Button(button_frame,text="*",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click('*'))             
one = Button(button_frame,text="1",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click(1))             
two= Button(button_frame,text="2",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click(2))             
three=Button(button_frame,text="3",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click(3))        
plus=Button(button_frame,text="+",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click('+'))             
zero=Button(button_frame,text="0",fg="black",width=21,height=3,bd=2,cursor="hand2",command=lambda:b_click(0))             
point=Button(button_frame,text=".",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_click('.'))
equals=Button(button_frame,text="=",fg="black",width=10,height=3,bd=2,cursor="hand2",command=lambda:b_equal())             

window.mainloop()
                 