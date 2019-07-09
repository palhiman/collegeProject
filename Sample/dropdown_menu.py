#!/usr/bin/env python3

from tkinter import *
import tkinter as tk

root = Tk()
root.title("Tk Dropdown examples")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky="nwes")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

# Create a tkinter variable
tkvar = StringVar(root)


# Dictionary with options
choices = {'Pizza', 'Lasagne', "Fries", "Potatoes"}
tkvar.set('Pizza') # set the default

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a dish").grid(row=1, column=1)
popupMenu.grid(row=2, column=1)


# on change dropdown value
def change_dropdown(*args):
    print(tkvar.get())


# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()