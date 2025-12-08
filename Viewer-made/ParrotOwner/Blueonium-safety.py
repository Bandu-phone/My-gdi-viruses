import time
import os
from tkinter import *
from tkinter import messagebox
from GDI_effects.GDI import *
from advancedpythonmalware import *


def start_malware():
    Effects.rainbow_blink(repeat=200)
    time.sleep(0)
    Effects.twisted_screen(repeat=70)
    time.sleep(0)
    Effects.flip_screen_upside_down(repeat=100)
    time.sleep(0)
    Effects.bw_screen(repeat=5)
    time.sleep(0)
    Effects.type__text("Blueonium.exe", repeat=100)
    time.sleep(0)
    Effects.super_icon_screen(repeat=20000)
    time.sleep(0)
    GDI.screen_glitch(repeat_time, r,g,b)
    time.sleep(1)


window = Tk()
label = Label(window, text="Are you sure you want to execute Gdi malware Blueonium.exe?")
label.grid(column=0,row=0)
button = Button(text="Yes", font=("Arial", 24), command=start_malware)
button.grid(column=0,row=1, padx=3, pady=3)
button = Button(text="No", font=("Arial", 24), command=lambda: window.destroy())
button.grid(column=1,row=1, padx=0, pady=0)
window.mainloop()





