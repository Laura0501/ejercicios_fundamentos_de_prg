#Declaración de variables
negativos=0
positivos=0
multiplos=0
sum_pares=0

#Inicio de ciclo
for n in range(10):
    numeros=int(input("Ingrese el numero: "))
    
    if numeros<0:
        negativos=negativos+1
        
    else:
        if numeros>0:
            positivos=positivos+1
    if numeros%15==0:
      multiplos=multiplos+1
    if numeros%2==0:
      sum_pares=sum_pares+numeros

print("La cantidad de numeros negativos de los valores ingresados es: ", negativos)
print("La cantidad de numeros positivos de los valores ingresados es: ", positivos)
print("La cantidad de numeros multiplos de 15, de los valores ingresados es: ", multiplos)
print("El acumulado de numeros pares de los valores ingresados es: ", sum_pares)