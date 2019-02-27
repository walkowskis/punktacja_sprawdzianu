try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    from tkinter import messagebox

grade = {'cel': 0.98,
         'bdb': 0.91,
         'db': 0.76,
         'dst': 0.51,
         'dop': 0.31}
grade_opinia = {'cel': 0.90,
                'bdb': 0.71,
                'db': 0.55,
                'dst': 0.40,
                'dop': 0.20}

class Punkty:
    def __init__(self, przecin, maxi, opinia):
        self.przecin=przecin
        self.maxi=maxi
        self.opinia = opinia

    def widelki(self):
        try:
            if self.opinia == False:
                dictList = []
                for key, value in grade.items():
                    dictList.append(round((value*int(self.maxi)),self.przecin))
                return dictList
            else:
                dictList = []
                for key, value in grade_opinia.items():
                    dictList.append(round((value*int(self.maxi)),self.przecin))
                return dictList
        except ValueError:
            messagebox.showinfo("Uwaga!", "Wprowadź poprawną wartość liczbową!")

    def prec(self, ocena):
        x=1
        y=10**self.przecin
        return round((ocena - (x/y)), self.przecin)

class MainFrame(Frame):
    """Klasa dla jednej
    z ramek """
    def __init__(self, my_window):
        super().__init__()
        self['relief']=RAISED
        #self['bd']=2
        self['padx']=15
        self['pady']=10
        self['width']=20
        self['height']=6

def licz():
    Spr = Punkty(w1.get(), Entry.get(E1), opinia.get())
    ocena = Punkty.widelki(Spr)
    def prec(x):
        return str(Punkty.prec(Spr, x))
    var = StringVar()
    oceny = Label(LF1, font=("Helvetica", 15), textvariable=var).grid(row=0, column=1)
    var.set(
            str(ocena[0])+ '  -  ' +str(Spr.maxi)+'\n'+
            str(ocena[1])+ '  -  ' +prec(ocena[0])+'\n'+
            str(ocena[2])+ '  -  ' +prec(ocena[1])+'\n'+
            str(ocena[3])+ '  -  ' +prec(ocena[2])+'\n'+
            str(ocena[4])+ '  -  ' +prec(ocena[3])+'\n'+
            '0  -  ' + prec(ocena[4])
            )

master = Tk()
frame_grade = Frame(master)
frame_scope = MainFrame(master)
frame_set = Frame(master)
frame_suwak = Frame(master)

#rozmiar i położeni okna
win_width = 304
win_height = 296
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
x_pos = (screen_width/2) - (win_width/2)
y_pos = (screen_height/2) - (win_height/2)
master.geometry('%dx%d+%d+%d' % (win_width, win_height, x_pos, y_pos))

master.title("WSO")

LF1=LabelFrame(frame_scope, labelanchor='n', fg="grey", text="Punktacja sprawdzianu", font=("Helvetica", 8))
LF1.grid(row=0, column=0)

#ułożenie w ramce frame_grade
L_marks = Label(LF1,  font=("Helvetica", 15), text="Celujący\nBardzo dobry\nDobry\nDostateczny\nDopuszczający\nNiedostateczny", anchor=E, justify=RIGHT)
L_marks.grid(row=0, column=0)

var = StringVar()
oceny = Label(LF1, width=18, textvariable=var).grid(row=0, column=1)
var.set('')

labelframe=LabelFrame(frame_set, padx=5, pady=5, labelanchor='n', fg="grey", text="Wpisz liczbę punktów", font=("Helvetica", 8))
labelframe.grid(row=0, column=0)

#input max pkt
E1 = Entry(labelframe, bd =4)
E1.grid(row=0,column=0)
E1.focus()

B1 = Button(labelframe, text ="Wylicz punktację",fg="blue", command = licz)
B1.grid(row=1,column=0)

opinia = BooleanVar()
ChB1 = Checkbutton(labelframe, text='Uczeń z opinią', var=opinia)
ChB1.grid(row=2, column=0)

#dzialanie i umiejscowienie suwaka:
w1 = Scale(labelframe, width=10, length=66, sliderlength=20, activebackground='blue', font=("Helvetica", 9), cursor='double_arrow', from_=0, to=5)
w1.grid(row=0, rowspan=3, column=1)
w1.set(1)

#ułożenie ramek
frame_grade.grid(row=0, column=0)
frame_scope.grid(row=0, column=0)
frame_set.grid(row=1, column=0)
#frame_suwak.grid(row=1, column=1)

master.mainloop()
