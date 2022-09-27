from tkinter import *
from tkinter import ttk
import mysql.connector as conn
from config import config

root = Tk()
root.title('window Title')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# entry data

def connectdb():
    params = config()
    connection = conn.connect(**params)
    
    return connection

cur = connectdb().cursor()

connection = connectdb()

def clear():
    pass

def submit():
    pass

# set label
continent = StringVar()
continent_entry = ttk.Entry(mainframe, width=20, textvariable=continent)
continent_entry.grid(column=2, row=2, sticky=(W,E))
continent_label = ttk.Label(mainframe,text='Continent').grid(column=1, row=2,sticky=W)



# submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0)

# quit button
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(row=9)

# entry point
root.mainloop()