#Declaración de variables
multiplos3=0
multiplos5=0

#Inicio del ciclo

for f in range(10):
    valor=int(input("Ingrese un valor:"))
    if valor%3==0:
        multiplos3=multiplos3+1
    if valor%5==0:
        multiplos5=multiplos5+1
print("Cantidad de valores ingresados múltiplos de 3 es: ", multiplos3)

print("Cantidad de valores ingresados múltiplos de 5 es: ", multiplos5)

