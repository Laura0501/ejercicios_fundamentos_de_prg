#Lecturas de archivos tipo excel
#Importar librerias

import pandas as pd

#Leer archivos excel
df_archivoexcel=pd.read_excel('ventas_productos_1.xlsx', index_col="Producto")
df_archivoexcel=df_archivoexcel[:10].copy()
print(df_archivoexcel)

print(df_archivoexcel)

#Grafica vertical
df_archivoexcel.plot(kind = 'bar')

#Grafica horizontal
df_archivoexcel.plot(kind = 'barh')

#Separación de barras
df_archivoexcel.plot(kind = 'barh' , width=1)#Cada grupo de barras ocupa todo el espacio
