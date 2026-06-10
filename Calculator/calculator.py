Python
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = Entry(root, width=25, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

def click(num):
    entry.insert(END, str(num))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('%',4,1),('^',4,2),('+',4,3)
]

for (text,row,col) in buttons:
    Button(root,text=text,width=5,height=2,
           command=lambda t=text: click('**' if t=='^' else t)
           ).grid(row=row,column=col)

Button(root,text="C",width=10,height=2,command=clear).grid(row=5,column=0,columnspan=2)
Button(root,text="=",width=10,height=2,command=calculate).grid(row=5,column=2,columnspan=2)

root.mainloop()
