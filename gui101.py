from tkinter import *
from tkinter import ttk,messagebox
from tkinter import colorchooser
from tkinter import filedialog
import sys
gui = Tk()
gui.title('Basic GUI Python')
gui.geometry('500x500')
# สร้างข้อความ
l1=Label(text='User Name :')
l2=Label(text='Password :')
e1=Entry(bd=5)
e2=Entry(bd=5)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)



gui.mainloop()




