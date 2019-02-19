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
        var1 = StringVar()
        l_cel = Label(top, textvariable=var1).grid(row=2, column=1)
        var1.set(to_str(cel) + ' - ' + to_str(point))
        var2 = StringVar()
        l_bdb = Label(top, textvariable=var2).grid(row=3, column=1)
        var2.set(to_str(bdb)+' - '+to_str(cel-0.01))
        var3 = StringVar()
        l_db = Label(top, textvariable=var3).grid(row=4, column=1)
        var3.set(to_str(db)+' - '+to_str(bdb-0.01))
        var4 = StringVar()
        l_dst = Label(top, textvariable=var4).grid(row=5, column=1)
        var4.set(to_str(dst)+' - '+to_str(db-0.01))
        var5 = StringVar()
        l_dop = Label(top, textvariable=var5).grid(row=6, column=1)
        var5.set(to_str(dop)+' - '+to_str(dst-0.01))
        var6 = StringVar()
        l_ndst = Label(top, textvariable=var6).grid(row=7, column=1)
        var6.set(to_str(0)+' - '+to_str(dop-0.01))
    except ValueError:
        messagebox.showinfo("Uwaga!","Wprowadź poprawne wartości liczbowe!")

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
E1.focus()

B1=Button(top, text ="Punktacja",command = punktacja).grid(row=8,columnspan=2,)
B2=Button(top, text ="Punktacja opinia",command = punktacja).grid(row=9,column=1,)
top.mainloop()
