import saaPohja
from tkinter import *


#def onKeyPress(event):
#    root.destroy()


root = Tk()
root.configure(background='black')
root.attributes('-fullscreen', True)
lampoTeksti = Label(root, text="lämpotila jyväskylässä on %s C"%(saaPohja.anna_lampo()))
lampoTeksti.config(font=("Courier", 44))
lampoTeksti.config(fg = 'white', bg = 'black')
lampoTeksti.pack()
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
#print(saaPohja.anna_lampo())