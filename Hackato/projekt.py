from tkinter import*
import tkinter.messagebox
from tkinter.ttk import*
from sqlite3 import *
from random import*
from calendar import Calendar

con=connect('baza.db')
cur=con.cursor()

class Prozor(Frame):
    def __init__(self, r):
        self.R = r
        super().__init__(self.R)
        self.R.title('Online kupovina karata')
        self.grid()
        self.R.geometry('405x90')
        self.R.resizable(False, False)
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        self.L1=Label(self, text='Online kupovina avionskih karata', font='Bold 20')
        self.L1.grid(column=1, row=1)
        self.B1=Button(self, text='Poništi kartu', command=self.PoništiKartu)
        self.B1.grid(column=1, row=2)
        self.B2=Button(self, text='Kupi kartu', command=self.KupiKartu)
        self.B2.grid(column=1, row=3)
        return

    def PoništiKartu(self):
        self.R.withdraw()
        self.PoništiKartu=Toplevel(self.R)
        bb=Prozor1(self.PoništiKartu)
        return

    def KupiKartu(self):
        self.R.withdraw()
        self.KupiKartu=Toplevel(self.R)
        bb=Prozor2(self.KupiKartu)
        return

class Prozor1(Frame):
    def __init__(self, r):
        self.R = r
        super().__init__(self.R)
        self.R.title('Online kupovina karata')
        self.grid()
        self.R.geometry('360x110')
        self.R.resizable(False, False)
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        self.L1=Label(self, text='Ime i prezime:')
        self.L1.grid(column=1, row=1)
        self.L3=Label(self, text='Mjesto polaska:')
        self.L3.grid(column=1, row=3)
        self.L4=Label(self, text='Broj računa:')
        self.L4.grid(column=1, row=2)

        self.E1=Entry(self, width=43)
        self.E1.grid(column=2, row=1)
        self.E2=Entry(self, width=43)
        self.E2.grid(column=2, row=2)
        f=open('airports.txt','r')
        airp= f.readlines()

        self.C2=Combobox(self, height=5, width=40, values=airp)
        self.C2.grid(column=2, row=3)
        
        self.B1=Button(self, text='Otkaži rezervaciju', command=self.OtkaziRezervaciju)
        self.B1.grid(column=2, row=5)

    def OtkaziRezervaciju(self):
        d=self.E1.get()
        b=self.E2.get()
        c=self.C2.get()
        cur=con.cursor()
        x=str(d)
        y=str(c)
        con.commit()
        if d=='' or b=='' or c=='':
             tkinter.messagebox.showerror("Oops","Sva polja moraju biti popunjena")
        else:
            cur.execute("delete from letovi where ID=(?) and ime=(?)",(b,d))
            tkinter.messagebox.showinfo("","Vaša rezervacija je otkazana!")       
        return

class Prozor2(Frame):
    def __init__(self, r):
        self.R = r
        super().__init__(self.R)
        self.R.title('Online kupovina karata')
        self.grid()
        self.R.geometry('360x160')
        self.R.resizable(False, False)
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        self.L1=Label(self, text='Mjesto polaska:')
        self.L1.grid(column=1, row=1)
        self.L2=Label(self, text='Mjesto dolaska:')
        self.L2.grid(column=1, row=2)
        self.L3=Label(self, text='Ime i prezime:')
        self.L3.grid(column=1, row=3)
        self.L4=Label(self, text='Vrsta karte:')
        self.L4.grid(column=1, row=4)
        self.L5=Label(self, text='Dan polaska:')
        self.L5.grid(column=1, row=5)
        self.L6=Label(self, text='Vrijeme polaska:')
        self.L6.grid(column=1, row=6)

        obj=Calendar()
        datumi=list()
        for day in obj.itermonthdates(2020,5):
            datumi.append(day)
        f=open('airports.txt','r')
        airp= f.readlines()

        mp=StringVar()
        self.C1=Combobox(self, textvariable=mp, height=5, width=40, values=airp[1::])
        self.C1.grid(column=2, row=1)
        md=StringVar()
        self.C2=Combobox(self, textvariable=md, height=5, width=40, values=airp[1::])
        self.C2.grid(column=2, row=2)
        vk=StringVar()
        self.C3=Combobox(self, textvariable=vk, height=5, width=40, values=["BusinessClass","Economic"])
        self.C3.grid(column=2, row=4)
        dp=StringVar()
        self.C4=Combobox(self, textvariable=dp, height=5, width=40, values=datumi)
        self.C4.grid(column=2, row=5)
        vp=StringVar()
        self.C5=Combobox(self, textvariable=vp, height=5, width=40, values=["1:00", "7:00","13:00","16:00","21:00"])
        self.C5.grid(column=2, row=6)

        ip=StringVar()
        self.E1=Entry(self, textvariable=ip, width=43)
        self.E1.grid(column=2, row=3)
        
        self.B1=Button(self, text='Odabir sjedala', command=self.OdabirSjedala)
        self.B1.grid(column=2, row=7)
        return

    def OdabirSjedala(self):
        a = self.C1.get()
        b = self.C2.get()
        c = self.C3.get()
        d = self.C4.get()
        f = self.C5.get()
        g = self.E1.get()
        self.X=[a,b,c,d,f,g]
        if a=='' or b=='' or c=='' or d=='' or f=='' or g=='':
            tkinter.messagebox.showerror("OOPS","Sva polja moraju biti popunjena")
        if a==b:
            tkinter.messagebox.showerror("Error","Mjesto polaska i dolaska ne može biti isto")
        else:    
            self.R.withdraw()
            bb=Prozor2_1(self.R, self.X)
        return (self.X)
    
class Prozor2_1(Toplevel):
    def __init__(self, r, x):
        self.R = r
        super().__init__(self.R)
        self.R.title('Online kupovina karata')
        self.grid()
        self.R.geometry('530x480')
        self.R.resizable(False, False)
        self.X = x
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        self.L1_1=Label(self, text='')
        self.L1_1.grid(column=1, row=1)
        self.L1_2=Label(self, text='', width=3)
        self.L1_2.grid(column=5, row=1)
##        self.L1_2.config(height=1, width=5)

        self.L1=Label(self, text='A')
        self.L1.grid(column=1, row=2)
        self.L2=Label(self, text='B')
        self.L2.grid(column=1, row=3)
        self.L3=Label(self, text='C')
        self.L3.grid(column=1, row=4)
        self.L4=Label(self, text='D')
        self.L4.grid(column=1, row=5)
        self.L5=Label(self, text='F')
        self.L5.grid(column=1, row=6)
        self.L6=Label(self, text='G')
        self.L6.grid(column=1, row=7)
        self.L7=Label(self, text='H')
        self.L7.grid(column=1, row=8)
        
        self.L8=Label(self, text='1')
        self.L8.grid(column=2, row=1)
        self.L9=Label(self, text='2')
        self.L9.grid(column=3, row=1)
        self.L10=Label(self, text='3')
        self.L10.grid(column=4, row=1)
        self.L11=Label(self, text='4')
        self.L11.grid(column=6, row=1)
        self.L12=Label(self, text='5')
        self.L12.grid(column=7, row=1)
        self.L13=Label(self, text='6')
        self.L13.grid(column=8, row=1)

        self.L16=Label(self, font=('Curier', 10), text='Odabrano sjedalo:')
        self.L16.grid(column=10, row=7)

        self.S=StringVar()
        self.L17=Label(self, textvariable=self.S)
        self.L17.grid(column=11, row=7)

        self.L18=Label(self, font=('Curier', 10), text='Cijena:')
        self.L18.grid(column=10, row=8)
        x=self.X
        f=open('airports.txt','r')
        airp= f.readlines()
        cijena=(int(airp.index(x[0]))+ int(airp.index(x[1])))*10
        self.S2=StringVar()
        self.L19=Label(self, textvariable=self.S2)
        self.L19.grid(column=11, row=8)
        self.S2.set(str(cijena)+'€')
        
        self.B7=Button(self, command=self.B1, width=3)
        self.B7.grid(column=2, row=3)
##        self.B7.config(height=3, width=5)
        self.B8=Button(self, command=self.B2, width=3)
        self.B8.grid(column=3, row=3)
##        self.B8.config(height=3, width=5)
        self.B9=Button(self, command=self.B3, width=3)
        self.B9.grid(column=4, row=3)
##        self.B9.config(height=3, width=5)
        self.B10=Button(self, command=self.B4, width=3)
        self.B10.grid(column=6, row=3)
##        self.B10.config(height=3, width=5)
        self.B11=Button(self, command=self.B5, width=3)
        self.B11.grid(column=7, row=3)
##        self.B11.config(height=3, width=5)
        self.B12=Button(self, command=self.B6, width=3)
        self.B12.grid(column=8, row=3)
##        self.B12.config(height=3, width=5)
        self.B13=Button(self, command=self.C1, width=3)
        self.B13.grid(column=2, row=4)
##        self.B13.config(height=3, width=5)
        self.B14=Button(self, command=self.C2, width=3)
        self.B14.grid(column=3, row=4)
##        self.B14.config(height=3, width=5)
        self.B15=Button(self, command=self.C3, width=3)
        self.B15.grid(column=4, row=4)
##        self.B15.config(height=3, width=5)
        self.B16=Button(self, command=self.C4, width=3)
        self.B16.grid(column=6, row=4)
##        self.B16.config(height=3, width=5)
        self.B17=Button(self, command=self.C5, width=3)
        self.B17.grid(column=7, row=4)
##        self.B17.config(height=3, width=5)
        self.B18=Button(self, command=self.C6, width=3)
        self.B18.grid(column=8, row=4)
##        self.B18.config(height=3, width=5)
        self.B19=Button(self, command=self.D1, width=3)
        self.B19.grid(column=2, row=5)
##        self.B19.config(height=3, width=5)
        self.B20=Button(self, command=self.D2, width=3)
        self.B20.grid(column=3, row=5)
##        self.B20.config(height=3, width=5)
        self.B21=Button(self, command=self.D3, width=3)
        self.B21.grid(column=4, row=5)
##        self.B21.config(height=3, width=5)
        self.B22=Button(self, command=self.D4, width=3)
        self.B22.grid(column=6, row=5)
##        self.B22.config(height=3, width=5)
        self.B23=Button(self, command=self.D5, width=3)
        self.B23.grid(column=7, row=5)
##        self.B23.config(height=3, width=5)
        self.B24=Button(self, command=self.D6, width=3)
        self.B24.grid(column=8, row=5)
##        self.B24.config(height=3, width=5)
        self.B25=Button(self, command=self.E1, width=3)
        self.B25.grid(column=2, row=6)
##        self.B25.config(height=3, width=5)
        self.B26=Button(self, command=self.E2, width=3)
        self.B26.grid(column=3, row=6)
##        self.B26.config(height=3, width=5)
        self.B27=Button(self, command=self.E3, width=3)
        self.B27.grid(column=4, row=6)
##        self.B27.config(height=3, width=5)
        self.B28=Button(self, command=self.E4, width=3)
        self.B28.grid(column=6, row=6)
##        self.B28.config(height=3, width=5)
        self.B29=Button(self, command=self.E5, width=3)
        self.B29.grid(column=7, row=6)
##        self.B29.config(height=3, width=5)
        self.B30=Button(self, command=self.E6, width=3)
        self.B30.grid(column=8, row=6)
##        self.B30.config(height=3, width=5)
        self.B31=Button(self, command=self.F1, width=3)
        self.B31.grid(column=2, row=7)
##        self.B31.config(height=3, width=5)
        self.B32=Button(self, command=self.F2, width=3)
        self.B32.grid(column=3, row=7)
##        self.B32.config(height=3, width=5)
        self.B33=Button(self, command=self.F3, width=3)
        self.B33.grid(column=4, row=7)
##        self.B33.config(height=3, width=5)
        self.B34=Button(self, command=self.F4, width=3)
        self.B34.grid(column=6, row=7)
##        self.B34.config(height=3, width=5)
        self.B35=Button(self, command=self.F5, width=3)
        self.B35.grid(column=7, row=7)
##        self.B35.config(height=3, width=5)
        self.B36=Button(self, command=self.F6, width=3)
        self.B36.grid(column=8, row=7)
##        self.B36.config(height=3, width=5)
        self.B37=Button(self, command=self.G1, width=3)
        self.B37.grid(column=2, row=8)
##        self.B37.config(height=3, width=5)
        self.B38=Button(self, command=self.G2, width=3)
        self.B38.grid(column=3, row=8)
##        self.B38.config(height=3, width=5)
        self.B39=Button(self, command=self.G3, width=3)
        self.B39.grid(column=4, row=8)
##        self.B39.config(height=3, width=5)
        self.B40=Button(self, command=self.G4, width=3)
        self.B40.grid(column=6, row=8)
##        self.B40.config(height=3, width=5)
        self.B41=Button(self, command=self.G5, width=3)
        self.B41.grid(column=7, row=8)
##        self.B41.config(height=3, width=5)
        self.B42=Button(self, command=self.G6, width=3)
        self.B42.grid(column=8, row=8)
##        self.B42.config(height=3, width=5)
        self.B43=Button(self, command=self.H1, width=3)
        self.B43.grid(column=2, row=9)
##        self.B43.config(height=3, width=5)      
        self.B44=Button(self, command=self.H2, width=3)
        self.B44.grid(column=3, row=9)
##        self.B44.config(height=3, width=5)
        self.B45=Button(self, command=self.H3, width=3)
        self.B45.grid(column=4, row=9)
##        self.B45.config(height=3, width=5)
        self.B46=Button(self, command=self.H4, width=3)
        self.B46.grid(column=6, row=9)
##        self.B46.config(height=3, width=5)
        self.B47=Button(self, command=self.H5, width=3)
        self.B47.grid(column=7, row=9)
##        self.B47.config(height=3, width=5)
        self.B48=Button(self, command=self.H6, width=3)
        self.B48.grid(column=8, row=9)
##        self.B48.config(height=3, width=5)
        self.B49=Button(self, text='Kupi kartu', command=self.Racun)
        self.B49.grid(column=10, row=9)
##        self.B49.config(height=2, width=15)
        self.B1=Button(self, command=self.A1, width=3)
        self.B1.grid(column=2, row=2)
##        self.B1.config(height=3, width=5)
        self.B2=Button(self, command=self.A2, width=3)
        self.B2.grid(column=3, row=2)
##        self.B2.config(height=3, width=5)
        self.B3=Button(self, command=self.A3, width=3)
        self.B3.grid(column=4, row=2)
##        self.B3.config(height=3, width=5)
        self.B4=Button(self, command=self.A4, width=3)
        self.B4.grid(column=6, row=2)
##        self.B4.config(height=3, width=5)
        self.B5=Button(self, command=self.A5, width=3)
        self.B5.grid(column=7, row=2)
##        self.B5.config(height=3, width=5)
        self.B6=Button(self, command=self.A6, width=3)
        self.B6.grid(column=8, row=2)
##        self.B6.config(height=3, width=5)
        return
    
    def A1(self):
        self.S.set('A1')

    def A2(self):
        self.S.set('A2')

    def A3(self):
        self.S.set('A3')

    def A4(self):
        self.S.set('A4')

    def A5(self):
        self.S.set('A5')

    def A6(self):
        self.S.set('A6')

    def B1(self):
        self.S.set('B1')

    def B2(self):
        self.S.set('B2')

    def B3(self):
        self.S.set('B3')

    def B4(self):
        self.S.set('B4')

    def B5(self):
        self.S.set('B5')

    def B6(self):
        self.S.set('B6')

    def C1(self):
        self.S.set('C1')

    def C2(self):
        self.S.set('C2')

    def C3(self):
        self.S.set('C3')

    def C4(self):
        self.S.set('C4')

    def C5(self):
        self.S.set('C5')

    def C6(self):
        self.S.set('C6')

    def D1(self):
        self.S.set('D1')

    def D2(self):
        self.S.set('D2')

    def D3(self):
        self.S.set('D3')

    def D4(self):
        self.S.set('D4')

    def D5(self):
        self.S.set('D5')

    def D6(self):
        self.S.set('D6')

    def E1(self):
        self.S.set('E1')

    def E2(self):
        self.S.set('E2')

    def E3(self):
        self.S.set('E3')

    def E4(self):
        self.S.set('E4')

    def E5(self):
        self.S.set('E5')

    def E6(self):
        self.S.set('E6')

    def F1(self):
        self.S.set('F1')

    def F2(self):
        self.S.set('F2')

    def F3(self):
        self.S.set('F3')

    def F4(self):
        self.S.set('F4')

    def F5(self):
        self.S.set('F5')

    def F6(self):
        self.S.set('F6')

    def G1(self):
        self.S.set('G1')

    def G2(self):
        self.S.set('G2')

    def G3(self):
        self.S.set('G3')

    def G4(self):
        self.S.set('G4')

    def G5(self):
        self.S.set('G5')

    def G6(self):
        self.S.set('G6')

    def H1(self):
        self.S.set('H1')

    def H2(self):
        self.S.set('H2')

    def H3(self):
        self.S.set('H3')

    def H4(self):
        self.S.set('H4')

    def H5(self):
        self.S.set('H5')

    def H6(self):
        self.S.set('H6')

    def Racun(self):
        sjedalo=self.S.get()
        x=self.X
        x.append(sjedalo)
        br=randint(1,1000)
        x.append(br)
        x2=tuple(x)
        cur.execute("insert into letovi values(?,?,?,?,?,?,?,?)",x2)
        con.commit()
        self.R.withdraw()        
        bb=Prozor2_2(self.R,x)
        return


class Prozor2_2(Toplevel and Prozor2_1):
    def _init_(self, r, x):
        self.R = r
        super()._init_(self.R,x)
        self.R.title('Online kupovina karata')
        self.grid()
        self.R.geometry('540x280')
        self.R.resizable(False, False)
        self.KreirajSucelje()
        self.X=x
        return

    def KreirajSucelje(self):
        print(self.X)
        tekst='''
    Mjesto polaska: {}
    Mjesto dolaska: {}
    Ime i prezime: {}
    Sjedalo: {} {}
    Datum polaska: {}
    Vrijeme polaska: {}
    Broj računa: {}
    Otkazati kartu možete pomoću broja računa
    hvala Vam na kupnji!'''.format(self.X[0],self.X[1],self.X[5],self.X[2],self.X[6],
                                   self.X[3],self.X[4],self.X[7])
        Prozor2_2=Text(self)
        Prozor2_2.insert(END,tekst)
        Prozor2_2.pack()
        return

p=Prozor(Tk())
