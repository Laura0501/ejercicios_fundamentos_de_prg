#Declaración de variables
suma=0

#Inicio del ciclo
for n in range(10):
    valors=int(input("Ingrese el valor: "))
    if n>=5:
        suma=suma+1
print("La suma de los ultimos 5 valores ingresados es: ", suma)
    