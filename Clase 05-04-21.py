matriz=[[7,8,3],[1,9,2],[4,6,5]]
print(matriz)

#suma de los elementos de la matriz 
sumele=0
for f in range(3):
    for c in range(3):
        sumele=sumele+matriz[f][c]
print("La suma de los elementos es: ", sumele)

#Imprimir la matriz
for f in range(3):
    for c in range(3):
        print("Dato ", matriz[f][c])

#Sumar la diagonal principal
sumadiagonal=0
for pos in range(3):
    sumadiagonal=sumadiagonal+matriz[pos][pos]
print("Diagonal principal", sumadiagonal)