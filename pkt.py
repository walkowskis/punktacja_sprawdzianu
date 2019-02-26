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
        self['bd']=2

def licz():
    Spr = Punkty(w1.get(), Entry.get(E1), opinia.get())
    ocena = Punkty.widelki(Spr)
    def prec(x):
        return str(Punkty.prec(Spr, x))
    var = StringVar()
    oceny = Label(frame_scope, textvariable=var).grid(row=0, column=0)
    var.set(
            str(ocena[0])+' - '+str(Spr.maxi)+'\n'+
            str(ocena[1])+' - '+prec(ocena[0])+'\n'+
            str(ocena[2]) + ' - ' + prec(ocena[1])+'\n'+
            str(ocena[3]) + ' - ' + prec(ocena[2])+'\n'+
            str(ocena[4]) + ' - ' + prec(ocena[3])+'\n'+
            '0 - ' + prec(ocena[4])
            )

master = Tk()
frame_grade = Frame(master)
frame_scope = MainFrame(master)
frame_set = Frame(master)
frame_suwak = Frame(master)

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
L_marks = Label(frame_grade, text="Celujący\nBardzo dobry\nDobry\nDostateczny\nDopuszczający\nNiedostateczny")
L_marks.grid(row=0)

var = StringVar()
oceny = Label(frame_scope, textvariable=var).grid(row=0, column=0)
var.set('pusto')

#input max pkt
E1 = Entry(frame_set, bd =5)
E1.grid(row=0,columnspan=2)
E1.focus()

B1 = Button(frame_set, text ="Wylicz punktację",command = licz)
B1.grid(row=1,column=1)

opinia = BooleanVar()
ChB1 = Checkbutton(frame_set, text='Uczeń z opinią', var=opinia)
ChB1.grid(row=2, column=1)

#dzialanie i umiejscowienie suwaka:
w1 = Scale(frame_suwak, from_=0, to=5)
w1.grid(row=0, column=0)

#ułożenie ramek
frame_grade.grid(row=0, column=0)
frame_scope.grid(row=0, column=1)
frame_set.grid(row=1, columnspan=2)
frame_suwak.grid(row=0, column=3)

master.mainloop()
