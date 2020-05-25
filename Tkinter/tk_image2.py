# tk_image2.py

import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage( file = "part_it_building.gif" )

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w = tk.Label( root, 
              compound = tk.CENTER,
              text = explanation, 
              image = logo).pack( side = "right" )

root.mainloop()
