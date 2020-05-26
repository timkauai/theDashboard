import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
from scraper import getTemp

root = tk.Tk()
root.config(cursor='dot red')

canvas = tk.Canvas(root, height=1024, width=1440, bg="#E5E5E5")
canvas.pack()

weather = tk.Frame(root, bg="#ffffff")
weather.place(relwidth=0.2, relheight=0.2,
              relx=0.1, rely=0.1)

list = getTemp()
highandlow = Label(weather, text="high:\tlow:\n" + list[0] + "\t" + list[1])
highandlow.pack()

wind = Label(weather, text="wind:\n" + list[2] + " mph", anchor="e")
wind.pack()

humidity = Label(weather, text="Humidity:\n" + list[3] + "%", anchor="e")
humidity.pack()

precip = Label(weather, text="precipitation:\n" +
               list[4] + " inches", anchor="e")
precip.pack()

root.title("Dashboard")

root.mainloop()
