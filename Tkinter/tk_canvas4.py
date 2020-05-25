# tk_canvas4.py
from tkinter import *

canvas_width = 190
canvas_height =190

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

w.create_oval(10,10,175,175)

mainloop()
