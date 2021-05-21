#PRACTICA 1 Con arreglos vectores 


#Almacenar en un vector las 5 notas del parcial

#Declarar el vector-lista
listaNotas=[] 
sumanotas=0.0
notasganadas=0
notasperdidas=0

#Asignar valores a la lista con ciclo
for postlista in range(5):
    #Leer desde teclado la nota 
    notaest=float(input("Digite la nota: "))
    sumanotas=sumanotas+notaest
    if notaest>=3.0:
        notasganadas=notasganadas+1
    else:
        if notaest<3.0:
            notasperdidas=notasperdidas+1
    promedio=sumanotas/5
        
    #Almacenamos la escalar en el arreglo
    listaNotas.append(notaest)
    
#Imprimir el arreglo
print(listaNotas)
print("La suma de las notas es: ", sumanotas)
print("El numero de notas ganadas son: ", notasganadas)
print("El numero de notas perdidas es: ", notasperdidas)
print("El promedio de todas las notas es: ", promedio)
#============================================================================
