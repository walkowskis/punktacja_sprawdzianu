try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
def punktacja():
    def to_str(x):
        y=str(round(x, 2))
        return y
    try:
        point=Entry.get(E1)
        point=int(point)
        cel=point*0.98
        bdb=point*0.91
        db=point*0.76
        Entry.insert(E2, 0, to_str(cel)+' - '+to_str(point))
        Entry.insert(E3, 0, to_str(bdb)+' - '+to_str(cel-0.01))
        Entry.insert(E4, 0, to_str(db)+' - '+to_str(bdb-0.01))
        print(Na5)
    except ValueError:
        messagebox.showinfo("Uwaga!","Please enter the value in integer")
def clear():
    E2.delete(0, 'end')
    E3.delete(0, 'end')
top = Tk()
top.title("WSO")
L1 = Label(top, text="Punktacja sprawdzianów",).grid(row=0,column=1)
L2 = Label(top, text="Max punków:",).grid(row=1,column=0)
L3 = Label(top, text="Celujący",).grid(row=2,column=0)
L4 = Label(top, text="Bardzo dobry",).grid(row=3,column=0)
L4 = Label(top, text="Dobry",).grid(row=4,column=0)
L5 = Label(top, text="Dostateczny",).grid(row=5,column=0)
L6 = Label(top, text="Dopuszczający",).grid(row=6,column=0)
L7 = Label(top, text="Niedostateczny",).grid(row=7,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =1)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =1)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =1)
E4.grid(row=4,column=1)
E5 = Entry(top, bd =1)
E5.grid(row=5,column=1)
E6 = Entry(top, bd =1)
E6.grid(row=6,column=1)
E7 = Entry(top, bd =1)
E7.grid(row=7,column=1)
B1=Button(top, text ="Punktacja",command = punktacja).grid(row=8,column=1,)
B2=Button(top, text ="Punktacja opinia",command = clear).grid(row=9,column=1,)
top.mainloop()
