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
        dst=point*0.51
        dop=point*0.31
        Entry.insert(E2, 0, to_str(cel)+' - '+to_str(point))
        Entry.insert(E3, 0, to_str(bdb)+' - '+to_str(cel-0.01))
        Entry.insert(E4, 0, to_str(db)+' - '+to_str(bdb-0.01))
        Entry.insert(E5, 0, to_str(dst)+' - '+to_str(db-0.01))
        Entry.insert(E6, 0, to_str(dop)+' - '+to_str(dst-0.01))
        Entry.insert(E7, 0, to_str(0)+' - '+to_str(dop-0.01))

    except ValueError:
        messagebox.showinfo("Uwaga!","Wprowadź poprawne wartości liczbowe!")
def clear():
    E2.delete(0, 'end')
    E3.delete(0, 'end')

top = Tk()
#rozmiar i położeni okna
win_width=500
win_height=500
screen_width=top.winfo_screenwidth()
screen_height=top.winfo_screenheight()
x_pos=(screen_width/2) - (win_width/2)
y_pos=(screen_height/2) - (win_height/2)
top.geometry('%dx%d+%d+%d' % (win_width, win_height, x_pos, y_pos))

top.title("WSO")

L1 = Label(top, text="Punktacja sprawdzianów",).grid(row=0,column=1)
L2 = Label(top, text="Max punków:",).grid(row=0,column=0)
L3 = Label(top, text="Celujący",).grid(row=2,column=0)
L4 = Label(top, text="Bardzo dobry",).grid(row=3,column=0)
L4 = Label(top, text="Dobry",).grid(row=4,column=0)
L5 = Label(top, text="Dostateczny",).grid(row=5,column=0)
L6 = Label(top, text="Dopuszczający",).grid(row=6,column=0)
L7 = Label(top, text="Niedostateczny", fg='Red', font='Bold').grid(row=7,column=0)

E1 = Entry(top, bd =5)
E1.grid(row=1,column=3)
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
