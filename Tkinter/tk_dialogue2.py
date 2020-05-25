# tk_dialogue2.py
from tkinter import *
from tkinter.filedialog import askopenfilename      

def callback():
    name= askopenfilename() 
    print(name)
    
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()
