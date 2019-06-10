import sqlite3
from ordenamiento import *

def nuevo_piloto():
    puntos=0
    #crear los datos del nuevo piloto
    name=input("Ingrese el nombre del piloto:")
    #Leer los datos de los pilotos ya existentes
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    micursor.execute("SELECT * FROM pilotos")
    check=micursor.fetchall()
    #Comprobar que el piloto no esta registrado
    for linea in check:
        if(linea[0]==name):
            return print("El piloto ya esta registrado")
        else:
            existe=False
    miconexion.commit
    miconexion.close
    if(existe==False): #registar nuevo piloto
        pais=input("Ingrese el pais del piloto:")
        escudo=input("Ingrese la escuderia a la que pertenece:")
        temporada=input("ingrese la temporada en la que participa el piloto:")
        datos=[name,pais,escudo,puntos,temporada]
        miconexion=sqlite3.connect("InfoPilotos")
        micursor=miconexion.cursor()
        micursor.execute("INSERT INTO pilotos VALUES(?,?,?,?,?)",datos)
        miconexion.commit()
        miconexion.close()
        print("Piloto registrado")
    else:
        print("error")

def clasificacion():
    listabase=[]
    acomodo=[]
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    micursor.execute("SELECT * FROM pilotos")
    lista=micursor.fetchall()
    for linea in lista:
        linea=list(linea)
        listabase.append(linea)
    for res in clasi(listabase):
        acomodo.append(res)
    acomodo.reverse()
    for fin in acomodo:#para printear las clasificaciones en consola
        print(fin)
    miconexion.commit()
    miconexion.close()


def puntos(): #Aritmetica de victorias,derrotas,canceladas para el puntaje
    name=input("Ingrese el nombre del piloto:")
    existe=0
    existe2=0
    #Comprobar si el piloto existe
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    micursor.execute("SELECT * FROM pilotos")
    check=micursor.fetchall()
    #Comprobar que el piloto no esta registrado
    for linea in check:
        if(linea[0]==name):
            existe=1
            escuderia=linea[2]
    miconexion.commit
    miconexion.close
    if(existe==0): #El piloto esta ya en la base de datos
        print("El piloto no existe")
    elif(existe==1): #registar nuevo piloto
        victorias=int(input("Ingrese la cantidad de victorias del piloto:"))
        derrotas=int(input("Ingrese la cantidad de derrotas del piloto:"))
        canceladas=int(input("Ingrese la cantidad de carreras abandonadas:"))
        podio=int(input("Ingrese la cantidad que ha quedado de segundo o tercero:"))
        total=int(input("Ingrese la cantidad de carreras en las que ha participado el piloto:"))
        RGP= int(((victorias+derrotas)/(total-canceladas))*100)
        REP= int(((victorias)/(total-canceladas))*100)
        #IGE= int((victorias/total)) para la escuderia
        print(RGP,REP)
        puntuacion(RGP,name)
        datos=[victorias,derrotas,canceladas,podio,total,RGP,REP,0,name]
        datos2=[name,escuderia,victorias,derrotas,canceladas,podio,total,RGP,REP,0]
        miconexion=sqlite3.connect("Escuderia")
        micursor=miconexion.cursor()
        micursor.execute("SELECT * FROM escuderia")
        check=micursor.fetchall()
        #Comprobar que el piloto no esta registrado
        for linea in check:
            if(linea[0]==name):
                existe2=1
            else:
                existe2=0
        miconexion.commit
        miconexion.close
        if(existe2==1):    #para actualizar los datos si ya esta aagregado en la otra base de datos
            miconexion=sqlite3.connect("Escuderia")
            micursor=miconexion.cursor()
            micursor.execute("UPDATE escuderia SET victorias=(?),derrotas=(?),abandonadas=(?),podio=(?),total_carreras=(?),RGP=(?),REP=(?),IGE=(?) WHERE name=(?)",datos)
            miconexion.commit()
            miconexion.close()
        elif(existe2==0): #para agregarlo a la otra base de datos si aun no lo esta
            miconexion=sqlite3.connect("Escuderia")
            micursor=miconexion.cursor()
            micursor.execute("INSERT INTO escuderia VALUES(?,?,?,?,?,?,?,?,?,?)",datos2)
            miconexion.commit()
            miconexion.close()
            
            
        

    
def puntuacion(puntaje,nick):#Para cambiar el puntaje en la base de datos
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    datos=[puntaje,nick]
    micursor.execute("UPDATE pilotos SET puntuacion=(?) WHERE nombre_piloto=(?)",datos)
    miconexion.commit()
    miconexion.close()

#para obtener la puntuacion de la escuderia y actualizarla si fuera necesario
def escuderia_info(escuderia):
    datos=[escuderia]
    victoriastotal=[]
    totalcarreras=[]
    miconexion=sqlite3.connect("Escuderia")
    micursor=miconexion.cursor()
    micursor.execute("SELECT victorias,total_carreras FROM escuderia WHERE escuderia=(?)",datos)
    check=micursor.fetchall()
    for linea in check:
        victoriastotal.append(linea[0])
        totalcarreras.append(linea[1])
    print(victoriastotal,totalcarreras)
    vic=suma_pila(victoriastotal,0,len(victoriastotal)-1)
    total=suma_pila(totalcarreras,0,len(totalcarreras)-1)
    print(vic,total)
    IGE= float((vic/total)) #para la escuderia
    print("La puntuacion de la escuderia:",escuderia,"es de",IGE,"puntos")
    miconexion.commit()
    miconexion.close()
    # para actualizar la puntuacion de la escuderia en la base de datos "escuderia"
    miconexion=sqlite3.connect("Escuderia")
    micursor=miconexion.cursor()
    datos2=[IGE,escuderia]
    micursor.execute("UPDATE escuderia SET IGE=(?) WHERE escuderia=(?)",datos2)
    miconexion.commit()
    miconexion.close()
    



#para sumar las victorias y total de carreras para la informacion de escuderia
def suma_pila(x,cont,fin):
    if(cont==fin):
        return x[cont]
    elif(cont<fin):
        return x[cont]+suma_pila(x,cont+1,fin)
    else:
        return "revisar"



    
    #Funciones para hacer cambios en los registros de la base de datos

#funcion para cambiar el pais de un piloto
def change_pais(name,pais):
    datos=[pais,name]
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    micursor.execute("UPDATE pilotos SET pais=(?) WHERE nombre_piloto=(?)",datos)
    miconexion.commit()
    miconexion.close()
    print("El pais del piloto:",name,"fue cambiado a",pais)
#funcion para cambiar de escuderia de un piloto
def change_escuderia(name,escuderia):
    datos=[escuderia,name]
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    micursor.execute("UPDATE pilotos SET escuderia=(?) WHERE nombre_piloto=(?)",datos)
    miconexion.commit()
    miconexion.close()
    print("La escuderia del piloto:",name,"fue cambiado a",escuderia)

#funcion para cambiar la temporada de un piloto
def change_temporada(name,temporada):
    datos=[temporada,name]
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    micursor.execute("UPDATE pilotos SET temporada=(?) WHERE nombre_piloto=(?)",datos)
    miconexion.commit()
    miconexion.close()
    print("La temporada del piloto:",name,"fue cambiado a",temporada)
