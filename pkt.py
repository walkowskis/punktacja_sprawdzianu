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
        l_cel = Label(frame_scope, textvariable=var1).grid(row=0, column=0)
        var1.set(to_str(cel) + ' - ' + to_str(point))
        var2 = StringVar()
        l_bdb = Label(frame_scope, textvariable=var2).grid(row=1, column=0)
        var2.set(to_str(bdb)+' - '+to_str(cel-0.01))
        var3 = StringVar()
        l_db = Label(frame_scope, textvariable=var3).grid(row=2, column=0)
        var3.set(to_str(db)+' - '+to_str(bdb-0.01))
        var4 = StringVar()
        l_dst = Label(frame_scope, textvariable=var4).grid(row=3, column=0)
        var4.set(to_str(dst)+' - '+to_str(db-0.01))
        var5 = StringVar()
        l_dop = Label(frame_scope, textvariable=var5).grid(row=4, column=0)
        var5.set(to_str(dop)+' - '+to_str(dst-0.01))
        var6 = StringVar()
        l_ndst = Label(frame_scope, textvariable=var6).grid(row=5, column=0)
        var6.set(to_str(0)+' - '+to_str(dop-0.01))
    except ValueError:
        messagebox.showinfo("Uwaga!","Wprowadź poprawne wartości liczbowe!")

master = Tk()
frame_grade = Frame(master)
frame_scope = Frame(master, bd=2, relief='solid')
frame_set = Frame(master)

#rozmiar i położeni okna
win_width = 220
win_height = 200
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x_pos = (screen_width/2) - (win_width/2)
y_pos = (screen_height/2) - (win_height/2)
master.geometry('%dx%d+%d+%d' % (win_width, win_height, x_pos, y_pos))

master.title("WSO")

#ułożenie w ramce frame_grade
L3 = Label(frame_grade, text="Celujący",).grid(row=0, sticky=E)
L4 = Label(frame_grade, text="Bardzo dobry",).grid(row=1, sticky=E)
L4 = Label(frame_grade, text="Dobry",).grid(row=2, sticky=E)
L5 = Label(frame_grade, text="Dostateczny",).grid(row=3,sticky=E)
L6 = Label(frame_grade, text="Dopuszczający",).grid(row=4,sticky=E)
L7 = Label(frame_grade, text="Niedostateczny", fg='Red', font='Bold').grid(row=5,sticky=E)

E1 = Entry(frame_set, bd =5)
E1.grid(row=0,columnspan=2)
E1.focus()

B1 = Button(frame_set, text ="Punktacja",command = punktacja).grid(row=1,column=1,)
B2 = Button(frame_set, text ="Punktacja opinia",command = punktacja).grid(row=1,column=0,)

#ułożenie ramek
frame_grade.grid(row=0, column=0)
frame_scope.grid(row=0, column=1)
frame_set.grid(row=1, columnspan=2)

master.mainloop()
