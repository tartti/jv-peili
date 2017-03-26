import saaPohja
from tkinter import *


def onKeyPress(event, self):
    self.root.destroy()

root = Tk()
root.attributes('-fullscreen', True)
theLabel = Label(root, text="lämpotila jyväskylässä on %s C"%(saaPohja.anna_lampo()))
theLabel.pack()
root.bind('<KeyPress>', onKeyPress())

root.mainloop()
#print(saaPohja.anna_lampo())