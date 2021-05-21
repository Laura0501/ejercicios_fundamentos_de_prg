#Declaración de variables
sup_mayor=0

#Entradas
num_trian=int(input("Ingrese la cantidad de triangulos a ejecutar: "))

#Inicio del ciclo
for t in range(num_trian):
    base=int(input("Ingrese la base del triangulo: "))
    altura=int(input("Ingrese la altura del triangulo:"))
    sup=(base*altura)/2
    
    print("La base del triangulo es:", base)
    print("La altura del triangulo es:", altura)
    print("La superficie del triangulo es: ", sup)
    
if sup>=12:
    sup_mayor=sup_mayor+1
    
print("La cantidad de triangulos con superficie mayor a 12 son: ", sup_mayor)
        
    
