#Declaraciòn de variables
x=1
suma=0

#Entradas
num_personas=int(input("Ingrese el numero de personas de las que conoce la altura:  "))

while x<=num_personas:
    alturas=float(input("Ingrese la altura: "))
    suma=suma+alturas
    x=x+1
    
#Salida

promedio=suma/num_personas
print("El promedio de las alturas de las personas es:", promedio)

