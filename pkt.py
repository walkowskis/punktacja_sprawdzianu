try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
def proces():
    def to_str(x):
        y=str(round(x, 3))
        return y
    try:
        point=Entry.get(E1)
        point=int(point)
        Na5=point*0.82
        Entry.insert(E2, 0, to_str(Na5)+' - '+to_str(point))
        Entry.insert(E3, 0, to_str(Na5-0.01))
        print(Na5)
    except ValueError:
        messagebox.showinfo("Uwaga!","Please enter the value in integer")
top = Tk()
top.title("CALCULATOR")
L1 = Label(top, text="Punktacja sprawdzianów",).grid(row=0,column=1)
L2 = Label(top, text="Max punków:",).grid(row=1,column=0)
L3 = Label(top, text=" 5 ",).grid(row=2,column=0)
L4 = Label(top, text=" 4 ",).grid(row=3,column=0)
L4 = Label(top, text="Answer",).grid(row=4,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B1=Button(top, text ="Punktacja",command = proces).grid(row=5,column=1,)
B2=Button(top, text ="Punktacja opinia",command = proces).grid(row=6,column=1,)
top.mainloop()