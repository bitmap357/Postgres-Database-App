from tkinter import *
import tkinter as tk

root = Tk()
canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="Add Data")
label.grid(row=0, column=1)

label = Label(frame, text="Name")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

root.mainloop()
