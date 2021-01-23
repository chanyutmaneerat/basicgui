from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import sys
def mHello():
    print('chanyut maneerat')

def hello(event=None):
    # Dialog Box
    # messagebox.showinfo(title='แสดงข้อความ',message='Hello User !')
    # messagebox.showwarning(title='แจ้งเตือน',message='มีไวรัสเข้ามาในเคื่องคอมพิวเตอร์')
    # messagebox.showerror(title='แจ้งเตือน',message='มีไวรัสเข้ามาในเคื่องคอมพิวเตอร์')
    # messagebox.askquestion(title='คุณต้องการลบข้อมูลหรือป่าว',message='ต้องการลบข้อมูล')
    status = messagebox.askyesno(title='คำยืนยัน',message='คุณต้องการปิดโปรแกรม')
    if status > 0 :
        sys.exit() #คำสั่งที่ใช้ในการปิดโปรแกรม

def fColor(event=None):
    # Color Dialog
    mycolor =colorchooser.askcolor()
    mlable = Label(text= mycolor)
    mlable.pack()

def fOpen(event=None):
    # filedialog
    myfile = filedialog.askopenfile()
    mlable = Label(text=myfile).pack()



# สร้างหน้าจอ
gui = Tk()
gui.geometry('500x600')
gui.title('Basic Gui Python')
# สร้างข้อความ
mlable = Label(text='chanyut',fg='#000',bg='pink')

# สร้างปุ่มกด
mlable.pack(ipadx=20,ipady=20,padx=10,pady=5)
mbutton = Button(text='submit',bg='red',command=mHello)
mbutton.pack(ipadx=40,ipady=20,pady=5)

b1 = Button(text='Hello')
b1.bind("<Button-1>",hello)
b1.pack()
b2 = Button(text='color')
b2.bind('<Button-1>',fColor)
b2.pack()
b3 = Button(text='select File')
b3.bind('<Button-1>',fOpen)
b3.pack()


# สร้าง textBox
objEntry = Entry().pack()

# สร้างเมนู
#เมนู File
menubar = Menu(gui)
fileMenu = Menu(menubar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save..As")
fileMenu.add_command(label="Close")


# เมนู Help
helpMenu = Menu(menubar,tearoff=0)
helpMenu.add_command(label="Contract")
helpMenu.add_command(label="Document")




menubar.add_cascade(label="File",menu=fileMenu)
menubar.add_cascade(label="Help",menu=helpMenu)
gui.config(menu=menubar)

#Radio Button
r1 = Radiobutton(text='ชาย',value=1).pack()
r2 = Radiobutton(text='หญิง',value=2).pack()

# Spin Box
spin1 = Spinbox(fro=-10,to=10,state=DISABLED).pack()

# Listbox
l1 = Listbox()
l1.insert(1,'python')
l1.insert(2,'JAVA')
l1.insert(2,'DATABASE')
l1.pack()

# Slider
s1 = Scale(orient = HORIZONTAL,width=20,fro=0,to=100,length=300,tickinterval= 10,sliderlength=60) 
s1.pack()
gui.mainloop()

