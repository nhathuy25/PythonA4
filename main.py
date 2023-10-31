import Classes
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename= "journal")
#App interface:
root.title("Gestion d'emploi du temps")
root.iconbitmap("./logo.png")
root.geometry('800x500')


root.mainloop()