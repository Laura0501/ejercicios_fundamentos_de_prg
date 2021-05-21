#Declaraciòn de variables

notas_ma=0
#notas_ma son las mayores

notas_me=0
#notas_me son notas menores

x=0

#Inicio del ciclo

while x<=9 :
    notas=int(input("Ingrese el valor de la nota del alumno: "))
    if notas>=7:
     notas_ma =notas_ma+1
    else: 
     notas_me=notas_me+1
    x=x+1
    
#Final del ciclo
print("Los alumnos que tienen notas mayores o iguales a 7 son: ", notas_ma)
print("Los alumnos que tienen notas menores a 7 son: ", notas_me)

