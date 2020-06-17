from tkinter import *
from tkinter import ttk
import converter as cv

OPTIONS = [
    "float8",
    "float32",
    "double64"
]


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(cv.conv(value, tipo.get()))
    except ValueError:
        meters.set("entrada incorreta")
        pass


root = Tk()
tipo = StringVar(root)
tipo.set(OPTIONS[0])
selctipo = OptionMenu(root, tipo, *OPTIONS)

root.title("ponto flutuante calculadora")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=12, textvariable=feet)
feet_entry.grid(column=1, row=1, sticky=(W, E))
selctipo.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=meters).grid(column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=1, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
