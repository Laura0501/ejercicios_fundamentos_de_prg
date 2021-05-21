#Declaración de variables
num_mayoi=0

#Entradas
canti_num=int(input("Ingrese la cantidad de valores a ejecutar: "))

#Inicio del ciclo
for f in range(canti_num):
    num=int(input("Ingrese el valor:"))
    
    if num>=1000:
        num_mayoi=num_mayoi+1
        
print("la cantidad de valores mayores o iguales a 1000 son : ", num_mayoi)
