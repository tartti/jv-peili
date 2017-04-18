import saaPohja
import time
from tkinter import *


def luoNakyma():
    global lampoTeksti
    lampoTeksti = Label(root, text="lämpotila jyväskylässä on %s C"%(saaPohja.anna_lampo()))
    lampoTeksti.config(font=("Courier", 44))
    lampoTeksti.config(fg = 'white', bg = 'black')
    lampoTeksti.pack()


def paivitaSaa():
    global lampoTeksti
    lampoTeksti.config(text = saaPohja.anna_lampo())
    root.after(2000, paivitaSaa)



root = Tk()
root.configure(background='black')
root.attributes('-fullscreen', True)
luoNakyma()
paivitaSaa()
root.bind("<Escape>", lambda e: root.destroy())
root.mainloop()



#print(saaPohja.anna_lampo())