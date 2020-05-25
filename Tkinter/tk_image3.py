# tk_image3.py

import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage( file = "part_it_building.gif" )

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w = tk.Label( root, 
              justify = tk.LEFT,
              compound = tk.BOTTOM,
              padx = 10, 
              text = explanation, 
              image = logo).pack( side = "right" )

root.mainloop()
