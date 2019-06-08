from tkinter import *
from tkinter import ttk
#from telemetry import read
ven1=Tk()
ven1.geometry("800x650")
ven1.title("Inicio")
esc=Label(ven1,text="Escudería: NjSarc").place(x=350,y=0)
temp=Label(ven1,text="Temporada: 2019").place(x=0,y=25)
est=Label(ven1,text="Estado del vehiculo:  ").place(x=300,y=25)
ind=Label(ven1,text="Indice de ganador: " ).place(x=600,y=25)
log=Label(ven1,text="Logo").place(x=75,y=100)
logo=PhotoImage(file="defaultescuderia.png")
logo=logo.subsample(2,2)
img=Label(ven1,image=logo).place(x=50,y=150)
patro=PhotoImage(file="Imperial.png")
patro=patro.subsample(2,2)
patrocinadores=Label(ven1,image=patro).place(x=450,y=150)
def about():
    about=Tk()
    about.title("About")
    about.geometry("800x650")
    TEC=Label(about,text="Instituto Tecnológico de Costa Rica").place(x=280,y=0)
    Sergio=Label(about,text="Sergio Ríos Campos 2019007977").place(x=280,y=50)
    #fotoSer
    Nacho=Label(about,text="Ignacio Lorenzo  Martinez 2019068171").place(x=280,y=100)
    #fotoNach
    Carrera=Label(about,text="Ingeniería en Computadores").place(x=280,y=150)
    curso=Label(about,text="Taller de Programación").place(x=280,y=200)
    grupo=Label(about,text="Grupo: 3").place(x=280,y=250)
    año=Label(about,text="Año: 2019").place(x=280,y=300)
    profesor=Label(about,text="Profesor: Pedro Gutiérrez").place(x=280,y=350)
    pais=Label(about,text="Costa Rica").place(x=280,y=400)
    versionPy=Label(about,text="Python 3.7.2").place(x=280,y=450)
    inicio=Button(about,text="Inicio", command=about.withdraw).place(x=280,y=610)

def pos():
    pos=Tk()
    pos.geometry("800x650")
    pos.title("Tabla de posiciones")
    def nuevo():
        n=Tk()
        n.title("Ingrese sus Datos")
        n.geometry("500x500")
        nombre=Label(n,text="Nombre").place(x=20,y=20)
        nom=Entry(n)
        nom.place(x=20,y=45)
        pais=Label(n,text="País").place(x=20,y=70)
        pa=Entry(n)
        pa.place(x=20,y=95)
        escuderia=Label(n,text="Escudería").place(x=20,y=120)
        esc=Entry(n)
        esc.place(x=20,y=145)
        temporada=Label(n,text="Temporada").place(x=20,y=170)
        temp=Entry(n)
        temp.place(x=20,y=195)
        def Agregar():
            n.withdraw()
            N=nom.get()
            P=pa.get()
            E=esc.get()
            T=temp.get()
            print(N,P,E,T)           
        agregar=Button(n,text="Agragar Piloto",command=Agregar).place(x=20,y=250)     
    new=Button(pos,text="Nuevo Piloto",command=nuevo).place(x=10,y=500)
    inicio=Button(pos,text="Inicio", command=pos.withdraw).place(x=10,y=610)
def test():
    test=Tk()
    c=Canvas(test,width=800,height=650)
    test.geometry("800x650")
    test.title("Test Drive")
    c.create_rectangle(0,400,800,650,fill="green")
    c.create_rectangle(0,0,800,400,fill="#9ae1f5")
    c.create_rectangle(230,390,310,530,fill="#464849")
    c.create_rectangle(490,390,570,530,fill="#464849")
    c.create_rectangle(675,25,790,60,fill="white")
    c.create_text(720,40,text='''"Nombre"''')
    c.create_rectangle(0,0,150,20,fill="white")
    c.create_text(70,10,text='''"Nombre del producto"''')
    c.create_rectangle(0,90,90,110,fill="white")
    c.create_text(40,100,text='''"Escuderia"''')
    c.create_rectangle(675,65,790,100,fill="white")
    c.create_text(730,82,text='''"Nacionalidad"''')
    c.create_polygon(400,400,100,650,700,650,fill="red")
    c.create_rectangle(700,250,780,290,fill="black")
    celeb=Button(test,text="Celebración",command=celebra).place(x=705,y=260)
    c.create_rectangle(700,300,780,340,fill="black")
    esp=Button(test,text="Especial",command=especial).place(x=705,y=310)
    poder=Entry(test)
    poder.place(x=338,y=490)
    def Pwm():
        p=""
        p+="pwm:"+poder.get()+";"
        from telemetry import myCar
        myCar.send(p)  
    pwm=Button(test,text="Pwm",command=Pwm).place(x=380,y=520) 
    c.place(x=0,y=0)

def celebra():
    from telemetry import root,get_log,send,sendShowID,read
def especial():
    print("EzpeChial")
def Logo():
    l=Tk()
    l.title("Escuderias")
    l.geometry("500x500")
    esc=StringVar()
    e=ttk.Combobox(l)
    e.place(x=180,y=30)
    e['values']=("Mercedes","Ferrari","McLaren","Infinity")
    e.current(0)
    e.config(state="readonly")
    def CLogo():
        esc=e.get()
        print(esc)
        if esc=="Ferrari"or esc=="McLaren" or esc=="Infinity":
            logo=PhotoImage(file="Ferrari.png")
            logo=logo.subsample(2,2)
            img=Label(ven1,image=logo).place(x=50,y=150)
            l.withdraw
        else:
            logo=PhotoImage(file="defaultescuderia.png")
            logo=logo.subsample(2,2)
            img=Label(ven1,image=logo).place(x=50,y=150)
            
    E=Button(l,text="Cambiar",command=CLogo).place(x=195,y=60)
    
cambEsc=Button(ven1,text="Cambiar Logo",command=Logo).place(x=30,y=400)
cambPatro=Button(ven1,text="Cambiar Patrocinadores",command=print("Q")).place(x=500,y=400)
About=Button(ven1,text="About",command=about).place(x=30,y=550)
Posiciones=Button(ven1,text="Tabla de Posiciones",command=pos).place(x=100,y=550)
Test=Button(ven1,text="Test Drive",command=test).place(x=250,y=550)
esc=StringVar()
ven1.mainloop()

