def f_cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def f_imprimir(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")


# bloque principal

lista=f_cargar()
f_imprimir(lista)