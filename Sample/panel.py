#!/usr/bin/env python3
# Creating 2-pane widgets

from tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane", bg="green")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane", bg="yellow")
m2.add(top)

bottom = Label(m2, text="bottom pane", bg="blue")
m2.add(bottom)

mainloop()
