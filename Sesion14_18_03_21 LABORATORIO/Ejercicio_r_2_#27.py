

def cargar_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def retornar_mayormenor(li):
    mayor=li[0]
    menor=li[0]
    for x in range(1,len(li)):
        if li[x]>mayor:
            mayor=li[x]
        else:
            if li[x]<menor:
                menor=li[x]
    return [mayor,menor]                


# bloque principal del programa

lista=cargar_lista()
rango=retornar_mayormenor(lista)
print("El mayor elemento de la lista:",rango[0])
print("El menor elemento de la lista:",rango[1])