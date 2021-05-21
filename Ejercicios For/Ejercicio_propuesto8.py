#Declaración de variables
suma1=0
suma2=0
suma3=0
promedio1=0
promedio2=0
promedio3=0

#Inicio del ciclo

print("Jornada Mañana")

for m in range(5):
    edades1=int(input("Ingrese la edad del estudiante: "))
    suma1=suma1+edades1
    promedio1=suma1/5
print("El promedio de edades del turno de la mañana es: ", promedio1)
    
print("Jornada Tarde")  
  
for n in range(6):
    edades2=int(input("Ingrese la edad del estudiante: "))
    suma2=suma2+edades2
    promedio2=suma2/6
print("El promedio de edades del turno de la tarde es: ", promedio2)

print("Jornada Noche")
for n in range(11):
    edades3=int(input("Ingrese la edad del estudiante: "))
    suma3=suma3+edades3
    promedio3=suma3/11
print("El promedio de edades del turno de la noche es: ", promedio3)
    
if promedio1>promedio2 and promedio1>promedio3:
    print("El turno de la mañana tiene promedio de edades mayor")
    
else:
    if promedio2>promedio3: 
        print("El turno de la tarde tiene promedio de edades mayor")
        
    else:
        print("El turno de la noche tiene promedio de edades mayor")
        

    
    