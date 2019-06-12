from tkinter import *
from tkinter import ttk
from data_base import*

#Funcion para elegir a la escuderia que se quiere entrar
def cambiar():
    e=Tk()
    e.title("Escudeía")
    e.geometry("500x500")
    e.resizable(False,False)
    e.config(bd=15)
    e.config(relief="sunken")
    ESC=Label(e,text="Elija una escudeía").place(x=20,y=20)
    esc=ttk.Combobox(e)
    esc['values']=("NjSarc","Mercedes","Ferrari","McLaren","Red Bull")
    esc.current(0)
    esc.config(state="readonly")
    esc.place(x=20,y=40)
    def mandar():
        e.withdraw()
        m=esc.get()
        if(m=="Mercedes"):
           logo=PhotoImage(file="imagenes\mercedes.png")
           patro=PhotoImage(file="imagenes\Imperial.png")
           Esc="Escudería: Mercedes"
           Ven1(logo,patro,Esc,m)
        elif(m=="Ferrari"):
            logo=PhotoImage(file="imagenes\errari.png")
            logo=logo.subsample(4,4)
            patro=PhotoImage(file="imagenes\pilsen.png")
            Esc="Escudería: Ferrari"
            Ven1(logo,patro,Esc,m)
        elif(m=="McLaren"):
            logo=PhotoImage(file="imagenes\mclaren.png")
            logo=logo.zoom(2,2)
            patro=PhotoImage(file="imagenes\heineken.png")
            Esc="Escudería: McLaren"
            Ven1(logo,patro,Esc,m)
        elif(m=="NjSarc"):
            logo=PhotoImage(file="imagenes\jSarc.png")
            logo=logo.subsample(1,1)
            patro=PhotoImage(file="imagenes\Bananacode.png")
            patro=patro.subsample(2,1)
            Esc="Escudería: NjSarc"
            Ven1(logo,patro,Esc,m)
        else:
            logo=PhotoImage(file="imagenes\edbull.png")
            patro=PhotoImage(file="imagenes\pirelli.png")
            patro=patro.subsample(6,6)
            Esc="Escudería: Red Bull"
            Ven1(logo,patro,Esc,m)
    ele=Button(e,text="Elegir",command=mandar).place(x=20,y=80)
def Ven1(logo,patro,Esc,m):
    IGE=escuderia_info(m)
    IGE= "Indice de ganador:  "+str(IGE)
    ven1=Toplevel()
    ven1.geometry("800x650")
    ven1.title("Inicio")
    ven1.resizable(False,False)
    ven1.config(bd=15)
    ven1.config(relief="sunken")
    esc=Label(ven1,text=Esc).place(x=350,y=0)
    temp=Label(ven1,text="Temporada: 2019").place(x=0,y=25)
    est=Label(ven1,text="Estado del vehiculo: ").place(x=300,y=25)
    ind=Label(ven1,text=IGE).place(x=525,y=25)
    log=Label(ven1,text="Logo").place(x=75,y=100)
    logo=logo.subsample(2,2)
    img=Label(ven1,image=logo).place(x=50,y=150)
    patro=patro.subsample(2,2)
    patrocinadores=Label(ven1,image=patro).place(x=450,y=150)
    #Informacion de los desarrolladores
    def about():
        about=Tk()
        about.title("About")
        about.geometry("800x650")
        about.resizable(False,False)
        about.config(bd=15)
        about.config(relief="sunken")
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
    def elegir_orden():
        orden=Tk()
        orden.title("Eliga el orden")
        orden.geometry("500x500")
        orden.resizable(False,False)
        mensaje_orden=Label(orden,text="Eliga el orden de la clasificacion").place(x=20,y=120)
        ordenes=ttk.Combobox(orden)
        ordenes['values']=("Menor a mayor RGP","Mayor a menor RGP","Menor a mayor REP","Mayor a menor REP")
        ordenes.current(0)
        ordenes.config(state="readonly")
        ordenes.place(x=20,y=145)
        def elegido_orden():
            orden.withdraw()
            frase=ordenes.get()
            print(frase)
            if(frase=="Menor a mayor RGP"):
                a=clasificacion()
                pos(a)
                orden.destroy()
            elif(frase=="Mayor a menor RGP"):
                a=clasificacion2()
                pos(a)
                orden.destroy()
            elif(frase=="Menor a mayor REP"):
                a=clasificacion4()
                pos(a)
                orden.destroy()
            elif(frase=="Mayor a menor REP"):
                a=clasificacion3()
                pos(a)
                orden.destroy()
            else:
                print("revisar ordenamiento de clasificaciones")
        orden_elegido=Button(orden,text="Elegir",command=elegido_orden).place(x=20,y=250)       
    def pos(a):
        pos=Tk()
        pos.geometry("800x650")
        pos.title("Tabla de posiciones")
        pos.resizable(False,False)
        pos.config(bd=15)
        pos.config(relief="sunken")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=0)
        cell.insert(0,"Nombre")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=1)
        cell.insert(0,"Pais")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=2)
        cell.insert(0,"Escuderia")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=3)
        cell.insert(0,"Puntuacion")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=4)
        cell.insert(0,"Temporada")
        from data_base import clasificacion
        i=0
        o=0
        global c
        c=1
        #Ciclo para mostar la clasificacion que se pide
        while(i!=len(a)):
            if(o==4):
                cell=Entry(pos,width=10)
                cell.grid(row=c,column=4)
                cell.insert(0,a[i][o])
                i+=1
                o=0
                c+=1
            else:
                cell=Entry(pos,width=10)
                cell.grid(row=c,column=o)
                cell.insert(0,a[i][o])
                i=i
                o+=1
        #Funcion para pedir los datos e  inscribir un nuevo piloto
        def nuevo():
            n=Tk()
            n.title("Ingrese sus Datos")
            n.geometry("500x500")
            n.config(bd=15)
            n.config(relief="sunken")
            nombre=Label(n,text="Nombre").place(x=20,y=20)
            nom=Entry(n)
            nom.place(x=20,y=45)
            pais=Label(n,text="País").place(x=20,y=70)
            pa=Entry(n)
            pa.place(x=20,y=95)
            escuderia=Label(n,text="Escudería").place(x=20,y=120)
            esc=ttk.Combobox(n)
            esc['values']=("NjSarc","Mercedes","Ferrari","McLaren","Red Bull")
            esc.current(0)
            esc.config(state="readonly")
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
                x=[N,P,E,T]
                from data_base import nuevo_piloto
                nuevo_piloto(N,P,E,int(T))
                            
            agregar=Button(n,text="Agragar Piloto",command=Agregar).place(x=20,y=250)     
        new=Button(pos,text="Nuevo Piloto",command=nuevo).place(x=10,y=500)
        inicio=Button(pos,text="Inicio", command=pos.withdraw).place(x=10,y=610)
    #Funcion para el testr drive(visualizacion de carro y controles)
    def eleccion_piloto():
        eleccion=Tk()
        eleccion.title("Eliga un piloto")
        eleccion.resizable(False,False)
        eleccion.geometry("500x500")
        lista_pilotos=pilotos_escuderia(m)
        texto_eliga=Label(eleccion,text="Eliga un piloto de su escuderia:").place(x=20,y=120)
        piloto=ttk.Combobox(eleccion)
        piloto['values']=lista_pilotos
        piloto.current(0)
        piloto.config(state="readonly")
        piloto.place(x=20,y=145)
        def seleccionar_piloto():
            eleccion.withdraw()
            name=piloto.get()
            test(name)
            eleccion.destroy()
        Elegir=Button(eleccion,text="Elegir",command=seleccionar_piloto).place(x=20,y=250)              
    def test(name):
        test=Tk()
        c=Canvas(test,width=800,height=650)
        test.geometry("800x650")
        test.title("Test Drive")
        test.resizable(False,False)
        test.config(bd=15)
        test.config(relief="sunken")
        c.create_rectangle(0,400,800,650,fill="green")
        c.create_rectangle(0,0,800,400,fill="#9ae1f5")
        c.create_rectangle(230,390,310,530,fill="#464849")
        c.create_rectangle(490,390,570,530,fill="#464849")
        c.create_rectangle(675,25,790,60,fill="white")
        c.create_text(720,40,text='''"Nombre"''')
        c.create_rectangle(0,0,150,20,fill="white")
        c.create_text(70,10,text='''"Nombre del producto"''')
        c.create_rectangle(0,90,90,110,fill="white")
        c.create_text(40,100,text=m)
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
        p=""
        p+="patron:especial;"
        from telemetry import myCar
        myCar.send(p)
    
    cambEsc=Button(ven1,text="Cambiar Logo",command=cambiar).place(x=30,y=400)
    cambPatro=Button(ven1,text="Cambiar Patrocinadores",command=print("Q")).place(x=500,y=400)
    About=Button(ven1,text="About",command=about).place(x=30,y=550)
    Posiciones=Button(ven1,text="Tabla de Posiciones",command=elegir_orden).place(x=100,y=550)
    Test=Button(ven1,text="Test Drive",command=eleccion_piloto).place(x=250,y=550)
    ven1.mainloop()

    
cambiar()
