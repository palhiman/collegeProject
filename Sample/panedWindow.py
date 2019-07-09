#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


window = tk.Tk()
window.title('Paned Window')
window.geometry('700x500')


pane = tk.PanedWindow(bg="green")
pane.pack(padx=5, pady=4)

left = Label(pane, text="Pane-1", bg="red", fg="white")
pane.add(left)

pane1 = PanedWindow(pane, orient=VERTICAL)
pane.add(pane1)

top = Label(pane1, text="Top Pane", bg="yellow", fg="cyan")
pane1.add(top)

window.mainloop()