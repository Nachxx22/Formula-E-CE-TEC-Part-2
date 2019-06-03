#funcion main
def clasi(x):
    if(len(x)==0):
        return 'error'
    else:
        return clasi_aux(len(x)-1,0,0,x)

#funcion auxiliar para tener las listas necesarias
def clasi_aux(fin,cont,stop,listabase):
    lista1=lista1_aux(listabase,cont,fin,[])
    listaord=merge(lista1)
    listanew=clasfin(listabase,listaord,fin,0,0,[])
    return listanew


#Hacer una lista de listas,, con toda la informacion de los pilotos
def clasfin(listabase,listaord,fin,cont,contm,listanew):
    if(contm==fin):
        if(listabase[cont][3]==listaord[contm]):
            listanew.append(listabase[cont])
            return listanew
        else:
            return clasfin(listabase,listaord,fin,cont+1,contm,listanew)
    elif(listabase[cont][3]==listaord[contm]):
        listanew.append(listabase[cont])
        return clasfin(listabase,listaord,fin,0,contm+1,listanew)
    else:
        return clasfin(listabase,listaord,fin,cont+1,contm,listanew)
            
            
    

#sacar los numeros para hacer una lista para acomodar segun puntaje(lista1)
def lista1_aux(x,cont,fin,listnew):
    if(cont==fin):
        if(x[cont][3]>0):
            listnew.append(x[cont][3])
            return listnew
        else:
            return'check error'
    elif(x[cont][3]>0):
        listnew.append(x[cont][3])
        return lista1_aux(x,cont+1,fin,listnew)
    else:
        return 'check error'


#Ordenamiento por mergesort, para la lista ordenada (listaord)
def merge(x):
    if(len(x) <= 1):
        return x   
    mediu = len(x) // 2
    izq=merge(x[:mediu])
    der=merge(x[mediu:])
    return merge_sort(izq,der)


def merge_sort(izq, der):
    izq_ind = 0
    der_ind = 0
    res = []
    while(izq_ind < len(izq) and der_ind < len(der)):
        if(izq[izq_ind] < der[der_ind]):
            res.append(izq[izq_ind])
            izq_ind += 1
        else:
            res.append(der[der_ind])
            der_ind += 1

    res += izq[izq_ind:]
    res += der[der_ind:]
    return res
