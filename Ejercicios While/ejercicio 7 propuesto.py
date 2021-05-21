#Declaracion de variables
x=1
num_pares=0
num_impares=0

#Inicio del ciclo
cant_num=int(input("Ingrese la cantidad de numeros enteros: "))

while x<=cant_num:
    numeros=int(input("Ingrese el numero: "))
    
    if numeros%2==0:
        num_pares=num_pares+1
    
    else:
        num_impares=num_impares+1
    x=x+1
    
print("La cantidad de numeros pares es: ", num_pares)
print("La cantidad de numeros impares es: ", num_impares)