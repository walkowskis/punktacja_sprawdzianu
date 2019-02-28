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
grade_expertise = {'cel': 0.90,
                'bdb': 0.71,
                'db': 0.55,
                'dst': 0.40,
                'dop': 0.20}

class Point:
    def __init__(self, precision, max_score, expertise):
        self.precision=precision
        self.max_score=max_score
        self.expertise = expertise

    def scope(self):
        try:
            if self.expertise == False:
                dictList = []
                for key, value in grade.items():
                    dictList.append(round((value*int(self.max_score)),self.precision))
                return dictList
            else:
                dictList = []
                for key, value in grade_expertise.items():
                    dictList.append(round((value*int(self.max_score)),self.precision))
                return dictList
        except ValueError:
            messagebox.showinfo("Uwaga!", "Wprowadź poprawną wartość liczbową!")

    def accuracy(self, mark):
        x=1
        y=10**self.precision
        return round((mark - (x/y)), self.precision)

class MainFrame(Frame):
    def __init__(self, my_window):
        super().__init__()
        self['padx']=15
        self['pady']=10
        self['width']=20
        self['height']=6

def calculate():
    test_set = Point(w1.get(), Entry.get(Input), expertise_var.get())
    mark = Point.scope(test_set)
    def prec(x):
        return str(Point.accuracy(test_set, x))
    var.set(
            str(mark[0])+ '  -  ' +str(test_set.max_score)+'\n'+
            str(mark[1])+ '  -  ' +prec(mark[0])+'\n'+
            str(mark[2])+ '  -  ' +prec(mark[1])+'\n'+
            str(mark[3])+ '  -  ' +prec(mark[2])+'\n'+
            str(mark[4])+ '  -  ' +prec(mark[3])+'\n'+
            '0  -  ' + prec(mark[4])
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
L_marks = Label(LF1,  font=("Helvetica", 15), text="Celujący\nBardzo dobry\nDobry\nDostateczny\nDopuszczający\nNiedostateczny", anchor=E, justify=RIGHT)
LF2=LabelFrame(frame_set, padx=5, pady=5, labelanchor='n', fg="grey", text="Wpisz liczbę punktów", font=("Helvetica", 8))
Input = Entry(LF2, bd =4)
Input.focus()
var = StringVar()
oceny = Label(LF1, font=("Helvetica", 15), width=12, textvariable=var).grid(row=0, column=1)
var.set('')
B1 = Button(LF2, text ="Wylicz punktację",fg="blue", command = calculate)
expertise_var = BooleanVar()
ChB1 = Checkbutton(LF2, text='Uczeń z opinią', var=expertise_var)
w1 = Scale(LF2, width=10, length=66, sliderlength=20, activebackground='blue', font=("Helvetica", 9), cursor='double_arrow', from_=0, to=5)
w1.set(1)

LF1.grid(row=0, column=0)
L_marks.grid(row=0, column=0)
LF2.grid(row=0, column=0)
Input.grid(row=0,column=0)
B1.grid(row=1,column=0)
ChB1.grid(row=2, column=0)
w1.grid(row=0, rowspan=3, column=1)

#ułożenie ramek
frame_grade.grid(row=0, column=0)
frame_scope.grid(row=0, column=0)
frame_set.grid(row=1, column=0)

master.mainloop()
