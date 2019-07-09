#!/usr/bin/env python3

from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title('paned Window')
root.geometry('500x200')

# create a panewindow
pane = PanedWindow(root, orient=HORIZONTAL)
pane.pack(fill=BOTH, expand=1)

# Adding some label widgets on panded window
row1 = LabelFrame(pane, text="pane1", bg="Red", width=10, height=10, padx=10)
pane.add(row1)

row2 = LabelFrame(pane, text="Fewwww", bg="green", width=10, height=10, padx=10)
pane.add(row2)



root.mainloop()
