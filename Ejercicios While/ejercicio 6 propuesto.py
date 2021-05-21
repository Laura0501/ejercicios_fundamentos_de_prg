#Declaración de variables 
suma_1=0
suma_2=0
x=1

#Inicio de ciclos

print("Lista 1")
while x<=15:
    lista_1=int(input("Ingrese el valor: "))
    suma_1=suma_1+lista_1
    x=x+1

print("lista 2")
x=1
while x<=15:
    lista_2=int(input("Ingrese el valor: "))
    suma_2=suma_2+lista_2
    x=x+1

print("acumulado lista 1:", suma_1)
print("acumulado lista 2:", suma_2)

if suma_1<suma_2:
    print("la lista con  mayor valor acumulado es la lista 2")
    
else :
    suma_2<suma_1
    print("la lista con  mayor valor acumulado es la lista 1")
    
