#Declaración de variables
equilatero=0
isoceles=0
escaleno=0

#Entradas
num_t=int(input("Ingrese el numero de triangulos a ejecutar: "))

#Inicio del ciclo
for t in range(num_t):
    lado1=int(input("Ingrese el primer lado del triangulo: "))
    lado2=int(input("Ingrese el segundo lado del triangulo: "))
    lado3=int(input("Ingrese el tercer lado del triangulo: "))
    
    if lado1==lado2 and lado1==lado3:
        equilatero=equilatero+1
        print("El triangulo es equilatero")
        
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            isoceles=isoceles+1
            print("El triangulo es isocele")
        
        else: 
            escaleno=escaleno+1
            print("El triangulo es escaleno")
        
print("La cantidad de triangulos equilateros es:", equilatero)
print("La cantidad de triangulos isoceles es:", isoceles)
print("La cantidad de triangulos escalenos es:", escaleno)
        
        