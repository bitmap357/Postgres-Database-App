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


def search(id):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="snow9823", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''Select * from student where id=%s'''
    cur.execute(query, id)
    row = cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()


def display_search(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, row)

def display_all():


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

label = Label(frame, text="Search")
label.grid(row=5, column=1)

label = Label(frame, text="Search by ID")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=6, column=2)

root.mainloop()
