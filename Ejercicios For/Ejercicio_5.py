#Declaración de variables 
alum_aprobados=0
alum_reprobados=0
#Inicio de ciclo
for f in range(10):
    nota=int(input("Ingrese la nota:"))
    if nota>=7:
        alum_aprobados=alum_aprobados+1
    else:
        alum_reprobados=alum_reprobados+1
        
print("Cantidad de alumnos aprobados es: ", alum_aprobados)

print("La cantidad de alumnos reprobados es: ", alum_reprobados)


