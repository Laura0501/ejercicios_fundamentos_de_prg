#Declaraciòn de variables 
x=1
suma=0
cobran_menos=0
cobran_mas=0

#Entrada 
num_emplea=int(input("Ingrese el numero de empleados: "))

#Inicio del ciclo
while x<=num_emplea:
    sueldos=int(input("Ingrese el sueldo: "))
    if  100<=sueldos<=300:
       cobran_menos=cobran_menos+1
    elif 300<=sueldos<=500:
       cobran_mas=cobran_mas+1
    suma=suma+sueldos
    x=x+1
    
print("Los empleados que ganan entre 100 y 300 son:", cobran_menos)
print("Los empleados que ganan mas de 300 son: ", cobran_mas)
print("El importe que gasta la empresa en sueldos es: ",suma )
