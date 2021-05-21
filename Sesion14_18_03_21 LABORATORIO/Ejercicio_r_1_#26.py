def sumarizar(lista):
    suma=0
    for s in range(len(lista)):
        suma=suma+lista[s]
    return suma


def mayor_num(lista):
    mayor=lista[0]
    for ma in range(1,len(lista)):
        if lista[ma]>mayor:
            mayor=lista[ma]
    return mayor


def menor_num(lista):
    men=lista[0]
    for me in range(1,len(lista)):
        if lista[me]<men:
            men=lista[me]
    return men
    

# bloque principal del programa

listavalores=[10, 56, 23, 120, 94]
print("La lista completa es:")
print(listavalores)
print("La suma de todos su elementos es", sumarizar(listavalores))
print("El mayor valor de la lista es", mayor_num(listavalores))
print("El menor valor de la lista es", menor_num(listavalores))