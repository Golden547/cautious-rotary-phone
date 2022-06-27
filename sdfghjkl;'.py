# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:17:31 2022

@author: shn99
"""

from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("900x600")
root.title("classes")

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createNewElement(self):
        label + Label(root,text = "A new Label has been created using this class", fg="red")
        label.pack()
        btn = Button(root, text="Button", command = self.message)
        btn.pack(padx=20, pady=10)
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")
        
obj_of_CreateElements = CreateElements()

btn = Button(root, text="Click to create label and button element", command= obj_of_CreateElements.createnewElement)
btn.pack(padx=20, pady = 10)

root.mainloop()
    