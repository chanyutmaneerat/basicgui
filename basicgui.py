from tkinter import *
from tkinter import messagebox
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
        

# สร้างหน้าจอ
gui = Tk()
gui.geometry('500x550')
gui.title('Basic Gui Python')
# สร้างข้อความ
mlable = Label(text='chanyut',fg='#000',bg='pink')

# สร้างปุ่มกด
mlable.pack(ipadx=20,ipady=20,padx=10,pady=10)
mbutton = Button(text='submit',bg='red',command=mHello)
mbutton.pack(ipadx=40,ipady=20,pady=20)

b1 = Button(text='Hello')
b1.bind("<Button-1>",hello)
b1.pack()



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
gui.mainloop()

