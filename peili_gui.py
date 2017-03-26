import saaPohja
from tkinter import *

root = Tk()
theLabel = Label(root, text="lämpotila jyväskylässä on %s C"%(saaPohja.anna_lampo()))
theLabel.pack()
root.mainloop()
#print(saaPohja.anna_lampo())