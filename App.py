from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()


def get_data(name, age, address):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="snow9823", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''INSERT INTO student(NAME, AGE, ADDRESS) VALUES (%s, %s, %s);'''
    cur.execute(query, (name, age, address))
    print('Data inserted')
    conn.commit()
    conn.close()


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

label = Label(frame, text="Age")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

label = Label(frame, text="Address")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button = Button(frame, text="Add", command=lambda: get_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

root.mainloop()
