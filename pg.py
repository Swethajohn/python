from tkinter import *
from tkinter.ttk import *
w=Tk()
w.title("GUI")
w.geometry('250x250')
# l1=Label(text='Hello World', fg='yellow', bg='red', font=('Arial',12,'bold'))
# l1.pack(fill=X,pady=50)
# l2=Label(text='Hello World', fg='yellow', bg='red')
# l2.pack(fill=X,pady=50)
e1=Entry(w)
e1.pack()
e2=Entry(w)
e2.pack()
e3=Entry(w)
e3.pack()
def add():
    s=int(e1.get())+int(e2.get())
    e3.delete(0)
    e3.insert(END,s)
    b1=Button(w,command=add,text='add').pack()
w.mainloop()                                       
