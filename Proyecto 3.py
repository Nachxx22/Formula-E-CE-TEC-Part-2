from tkinter import *
from tkinter import ttk
from data_base import*

#Funcion para elegir a la escuderia que se quiere entrar
def cambiar():
    e=Tk()
    e.title("Escudería")
    e.geometry("500x500")
    e.resizable(False,False)
    e.config(bd=15)
    e.config(relief="sunken")
    ESC=Label(e,text="Elija una escudería").place(x=20,y=20)
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
           geo="Ubicacion geografica: Alemania"
           Ven1(logo,patro,Esc,m,geo)
        elif(m=="Ferrari"):
            logo=PhotoImage(file="imagenes\errari.png")
            logo=logo.subsample(4,4)
            patro=PhotoImage(file="imagenes\pilsen.png")
            Esc="Escudería: Ferrari"
            geo="Ubicacion geografica: Italia"
            Ven1(logo,patro,Esc,m,geo)
        elif(m=="McLaren"):
            logo=PhotoImage(file="imagenes\mclaren.png")
            logo=logo.zoom(2,2)
            patro=PhotoImage(file="imagenes\heineken.png")
            Esc="Escudería: McLaren"
            geo="Ubicacion geografica: Reino Unido"
            Ven1(logo,patro,Esc,m,geo)
        elif(m=="NjSarc"):
            logo=PhotoImage(file="imagenes\jSarc.png")
            logo=logo.subsample(1,1)
            patro=PhotoImage(file="imagenes\Bananacode.png")
            patro=patro.subsample(2,1)
            Esc="Escudería: NjSarc"
            geo="Ubicacion geografica: Costa Rica"
            Ven1(logo,patro,Esc,m,geo)
        else:
            logo=PhotoImage(file="imagenes\edbull.png")
            patro=PhotoImage(file="imagenes\pirelli.png")
            patro=patro.subsample(6,6)
            Esc="Escudería: Red Bull"
            geo="Ubicacion geografica: Austria"
            Ven1(logo,patro,Esc,m,geo)
    ele=Button(e,text="Elegir",command=mandar).place(x=20,y=80)
def Ven1(logo,patro,Esc,m,geo):
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
    geografia=Label(ven1,text=geo).place(x=0,y=50)
    est=Label(ven1,text="Estado del vehiculo: Disponible").place(x=300,y=25)
    ind=Label(ven1,text=IGE).place(x=525,y=25)
    log=Label(ven1,text="Logo").place(x=75,y=100)
    logo=logo.subsample(2,2)
    img=Label(ven1,image=logo).place(x=50,y=150)
    patro=patro.subsample(2,2)
    patrocinadores=Label(ven1,image=patro).place(x=450,y=150)
    #Informacion de los desarrolladores
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
                nuevo_piloto(N,P,E,int(T))
                            
            agregar=Button(n,text="Agragar Piloto",command=Agregar).place(x=20,y=250)
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
        cell.config(state="readonly")
        cell.config(bg="white")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=1)
        cell.insert(0,"Pais")
        cell.config(state="readonly")
        cell.config(bg="white")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=2)
        cell.insert(0,"Escuderia")
        cell.config(state="readonly")
        cell.config(bg="white")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=3)
        cell.insert(0,"Puntuacion")
        cell.config(state="readonly")
        cell.config(bg="white")
        cell=Entry(pos,width=10)
        cell.grid(row=0,column=4)
        cell.insert(0,"Temporada")
        cell.config(state="readonly")
        cell.config(bg="white")
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
                cell.config(state="readonly")
                cell.config(bg="white")
            elif(i==10):
                return "ready"
            else:
                cell=Entry(pos,width=10)
                cell.grid(row=c,column=o)
                cell.insert(0,a[i][o])
                i=i
                o+=1
                cell.config(state="readonly")
                cell.config(bg="white")
         
        #Funcion para pedir los datos y agregar puntuacion
        def editar_piloto():
                pilotos=pilotos_all()
                edit=Tk()
                edit.title("Modificacion de piloto")
                edit.geometry("300x300")
                edit.config(bd=15)
                edit.config(relief="sunken")
                text=Label(edit,text="Eliga el piloto que quiere editar:").place(x=10,y=40)
                piloto=ttk.Combobox(edit)
                piloto['values']= pilotos
                piloto.current(0)
                piloto.config(state="readonly")
                piloto.place(x=10,y=65)
                def cambiar_pais():
                    cambp=Tk()
                    cambp.geometry("350x350")
                    cambp.title("Cambiando pais")
                    cambp.config(bd=15)
                    cambp.config(relief="sunken")
                    text=Label(cambp,text="Nuevo pais del piloto:").place(x=10,y=60)
                    pa=Entry(cambp)
                    pa.place(x=10,y=90)
                    def cambio_pais():
                        name=piloto.get()
                        pais=pa.get()
                        change_pais(name,pais)
                        cambp.destroy()
                        edit.destroy()
                    def volver():
                        cambp.destroy()
                    
                    elegirpais=Button(cambp,text="Cambiar",command=cambio_pais).place(x=10,y=145)
                    cerrarpais=Button(cambp,text="Volver",command=volver).place(x=80,y=145)
                def cambiar_escuderia():
                    cambe=Tk()
                    cambe.geometry("350x350")
                    cambe.title("Cambiando escuderia")
                    cambe.config(bd=15)
                    cambe.config(relief="sunken")
                    text=Label(cambe,text="Nueva escuderia del piloto:").place(x=10,y=60)
                    esc=ttk.Combobox(cambe)
                    esc['values']=("NjSarc","Mercedes","Ferrari","McLaren","Red Bull")
                    esc.current(0)
                    esc.config(state="readonly")
                    esc.place(x=10,y=90)
                    def cambio_escuderia():
                        name=piloto.get()
                        escuderia= esc.get()
                        change_escuderia(name,escuderia)
                        cambe.destroy()
                        edit.destroy()
                    def volver():
                        cambe.destroy()
                    
                    elegirpais=Button(cambe,text="Cambiar",command=cambio_escuderia).place(x=10,y=145)
                    cerrarpais=Button(cambe,text="Volver",command=volver).place(x=80,y=145)
                def cambiar_temporada():
                    cambt=Tk()
                    cambt.geometry("350x350")
                    cambt.title("Cambiando temporada")
                    cambt.config(bd=15)
                    cambt.config(relief="sunken")
                    text=Label(cambt,text="Nueva temporada del piloto:").place(x=10,y=60)
                    temporada=Entry(cambt)
                    temporada.place(x=10,y=90)
                    def cambio_temporada():
                        name=piloto.get()
                        temp=temporada.get()
                        change_temporada(name,temp)
                        cambt.destroy()
                        edit.destroy()
                    def volver():
                        cambt.destroy()
                    
                    elegirpais=Button(cambt,text="Cambiar",command=cambio_temporada).place(x=10,y=145)
                    cerrarpais=Button(cambt,text="Volver",command=volver).place(x=80,y=145)
                def eliminar_piloto():
                    cambpi=Tk()
                    cambpi.geometry("405x350")
                    cambpi.title("Eliminar piloto")
                    cambpi.config(bd=15)
                    cambpi.config(relief="sunken")
                    text=Label(cambpi,text="El piloto se eliminara para siempre").place(x=10,y=60)
                    text2=Label(cambpi,text="Presione el boton eliminar si esta seguro, si no lo esta presione volver").place(x=10,y=90)
                    def eliminar_pilotoo():
                        name=piloto.get()
                        eliminaar_piloto(name)
                        cambpi.destroy()
                        edit.destroy()
                    def volver():
                        cambpi.destroy()
                    
                    elegirpais=Button(cambpi,text="Eliminar",command=eliminar_pilotoo).place(x=10,y=145)
                    cerrarpais=Button(cambpi,text="Volver",command=volver).place(x=80,y=145)



                changepais=Button(edit,text="Cambiar País",command=cambiar_pais).place(x=30,y=100)
                changeescuderia=Button(edit,text="Cambiar Escuderia",command=cambiar_escuderia).place(x=30,y=130)
                changetemporada=Button(edit,text="Cambiar Temporada",command=cambiar_temporada).place(x=30,y=160)
                eliminarpiloto=Button(edit,text="Eliminar piloto",command=eliminar_piloto).place(x=30,y=190)

        def nuevo():
            pilotos=pilotos_all()
            n=Tk()
            n.title("Ingrese sus Datos")
            n.geometry("500x500")
            n.config(bd=15)
            n.config(relief="sunken")
            nombre=Label(n,text="Nombre del piloto:").place(x=20,y=20)
            nom=ttk.Combobox(n)
            nom['values']= pilotos
            nom.current(0)
            nom.config(state="readonly")
            nom.place(x=20,y=45)
            Victorias=Label(n,text="Victorias del piloto:").place(x=20,y=70)
            Vic=Entry(n)
            Vic.place(x=20,y=95)
            Derrotas=Label(n,text="Derrotas del piloto:").place(x=20,y=120)
            Der=Entry(n)
            Der.place(x=20,y=145)
            Canceladas=Label(n,text="Carreras canceladas del piloto:").place(x=20,y=170)
            Can=Entry(n)
            Can.place(x=20,y=195)
            Podio=Label(n,text="Carreras que estuvo en el podio:").place(x=20,y=220)
            Pod=Entry(n)
            Pod.place(x=20,y=245)
            def Agregar():
                n.withdraw()
                N=nom.get()
                V=Vic.get()
                D=Der.get()
                C=Can.get()
                P=Pod.get()
                T=int(V)+int(D)+int(C)+int(P)
                from data_base import nuevo_piloto
                puntos(N,int(V),int(D),int(C),int(P),int(T))
                            
            agregar=Button(n,text="Mandar datos",command=Agregar).place(x=20,y=280)

        new=Button(pos,text="Agregar/Actualizar puntos",command=nuevo).place(x=10,y=500)
        inicio=Button(pos,text="Inicio", command=pos.withdraw).place(x=10,y=400)
        modificar=Button(pos,text="Modificar piloto",command=editar_piloto).place(x=10,y=450)
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
        piloto=elegir_piloto(name)
        Nombre="Nombre: "+piloto[0]
        nacionalidad="Nacionalidad: "+piloto[1]
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
        c.create_text(720,40,text=Nombre)
        c.create_rectangle(0,0,150,20,fill="white")
        c.create_text(70,10,text='''"Nombre del producto"''')
        c.create_rectangle(0,90,90,110,fill="white")
        c.create_text(40,100,text=m)
        c.create_rectangle(642,65,790,100,fill="white")
        c.create_text(710,82,text=nacionalidad)
        c.create_polygon(400,400,100,650,700,650,fill="red")
        c.create_rectangle(700,250,780,290,fill="black")
        c.create_rectangle(700,300,780,340,fill="black")
        poder=Entry(test)
        poder.place(x=338,y=490)
        global ledstraseras
        global ledsfrontales
        global direccionalizq
        global direccionalder
        ledstraseras=0
        ledsfrontales=0
        direccionalizq=0
        direccionalder=0
        def Pwm():
            p=""
            p+="pwm:"+poder.get()+";"
            from telemetry import myCar
            myCar.send(p)  
        pwm=Button(test,text="Pwm",command=Pwm).place(x=380,y=520) 
        c.place(x=0,y=0)
        def celebra():
            print("celebracion")
            from telemetry import root,get_log,send,sendShowID,read
        def especial():
            print("especial")
            p=""
            p+="patron:especial;"
            from telemetry import myCar
            myCar.send(p)
        def leds_traseras():
            global ledstraseras
            if(ledstraseras==0):
                print("Leds traseras encendidas")
                ledstraseras=1
                from telemetry import myCar
                p="lb:1;"
                myCar.send(p)
            elif(ledstraseras==1):
                print("Leds traseras apagadas")
                ledstraseras=0
                from telemetry import myCar
                p="lb:0;"
                myCar.send(p)
            else:
                print("revisar leds traseras")
        def leds_frontales():
            global ledsfrontales
            if(ledsfrontales==0):
                print("Leds frontales encendidas")
                ledsfrontales=1
                from telemetry import myCar
                p="lf:1;"
                myCar.send(p)
            elif(ledsfrontales==1):
                print("Leds frontales apagadas")
                ledfrontales=0
                from telemetry import myCar
                p="lf:0;"
                myCar.send(p)
            else:
                print("revisar leds frontales")
        def leds_izquierda():
            global direccionalizq
            if(direccionalizq==0):
                print("Led izquierda encendida")
                direccionalizq=1
                from telemetry import myCar
                p="ll:1;"
                myCar.send(p)
            elif(direccionalizq==1):
                print("Led izquierda apagada")
                direccionalizq=0
                from telemetry import myCar
                p="ll:0;"
                myCar.send(p)
            else:
                print("revisar led izquierda")
        def leds_derecha():
            global direccionalder
            if(direccionalder==0):
                print("Led derecha encendida")
                direccionalder=1
                from telemetry import myCar
                p="lr:1;"
                myCar.send(p)
            elif(direccionalder==1):
                print("Led derecha apagada")
                direccionalder=0
                from telemetry import myCar
                p="lr:0;"
                myCar.send(p)
            else:
                print("revisar led derecha")
        def freno():
            print("Detenido")
            from telemetry import myCar
            p="pwm:0;"
            myCar.send(p)
                
                
        frenar=Button(test,text="Frenar",command=freno).place(x=250,y=410)
        traseras=Button(test,text="Luces traseras",command=leds_traseras).place(x=350,y=570)
        frontales=Button(test,text="Luces frontales",command=leds_frontales).place(x=350,y=410)
        izquierda=Button(test,text="Direcional izquierda",command=leds_izquierda).place(x=200,y=500)
        derecha=Button(test,text="Direcional derecha",command=leds_derecha).place(x=500,y=500)
        celeb=Button(test,text="Celebración",command=celebra).place(x=705,y=260)
        esp=Button(test,text="Especial",command=especial).place(x=705,y=310)
    
    cambEsc=Button(ven1,text="Cambiar Logo",command=cambiar).place(x=30,y=400)
    cambPatro=Button(ven1,text="Cambiar Patrocinadores",command=print("Q")).place(x=500,y=400)
    About=Button(ven1,text="About",command=about).place(x=30,y=550)
    Posiciones=Button(ven1,text="Tabla de Posiciones",command=elegir_orden).place(x=100,y=550)
    Test=Button(ven1,text="Test Drive",command=eleccion_piloto).place(x=250,y=550)
    new=Button(ven1,text="Nuevo Piloto",command=nuevo).place(x=345,y=550)
    ven1.mainloop()

    
cambiar()
