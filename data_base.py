import sqlite3
from ordenamiento import *


def nuevo():
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
            existe=True
        else:
            existe=False
    miconexion.commit
    miconexion.close
    if(existe==True): #El piloto esta ya en la base de datos
        print("El piloto ya esta registrado")

    elif(existe==False): #registar nuevo piloto
        pais=input("Ingrese el pais del piloto:")
        escudo=input("Ingrese la escuderia a la que pertenece:")
        puntos=0
        datos=[name,pais,escudo,puntos]
        miconexion=sqlite3.connect("InfoPilotos")
        micursor=miconexion.cursor()
        micursor.execute("INSERT INTO pilotos VALUES(?,?,?,?)",datos)
        miconexion.commit()
        miconexion.close()
        print("Piloto registrado")
    else:
        print("error")

def clasificacion(listabase):
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    micursor.execute("SELECT * FROM pilotos")
    lista=micursor.fetchall()
    for linea in lista:
        linea=list(linea)
        print(linea)
        listabase.append(linea)
    print(clasi(listabase))
    miconexion.commit()
    miconexion.close()



def puntuacion(puntaje):
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor
    
    

#Agregar los datos del piloto
    """
    miconexion=sqlite3.connect("InfoPilotos")
    micursor=miconexion.cursor()
    micursor.execute("INSERT INTO pilotos VALUES(?,?,?,?)",datos)
    miconexion.commit()
    miconexion.close()
    """



#para convertir en lista los datos de la base de datos
    """
    check=check[0]
    check=list(check)
    check=check[0]
    """
