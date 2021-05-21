#Declaración de variables 
cuadran1=0
cuadran2=0
cuadran3=0
cuadran4=0

#Entradas
cant=int(input("Cantidad de puntos a procesar: "))

#Inicio del ciclo
for c in range(cant):
    x=int(input("Ingrese el valor de x: "))
    y=int(input("Ingrese el valor de y: "))
    
    if x>0 and y>0:
        cuadran1=cuadran1+1
    else:
        if x<0 and y>0:
            cuadran2=cuadran2+1
        else:
            if x<0 and y<0:
                cuadran3=cuadran3+1
            else:
                if x>0 and y<0:
                    cuadran4=cuadran4+1

print("Los puntos en el primer cuadrante son: ", cuadran1)
print("Los puntos en el segundo cuadrante son: ", cuadran2)
print("Los puntos en el tercer cuadrante son: ", cuadran3)
print("Los puntos en el cuarto cuadrante son: ", cuadran4)