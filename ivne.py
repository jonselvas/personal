import pandas as pd
vcuentatotal=0
vestatus1='ATENDIDO'
vestatus2='PENDIENTE'
vestatus3='CANCELADO'
columnas=[]
columnasdatos=[]
union=[]


with open('GTYAB684_scmae_prog_entr.lst', 'r') as archivo:
    file = open("copy.txt", "w", newline='')
    linea = archivo.readline()

    for linea in archivo:
        if vestatus1 in linea or vestatus2 in linea or vestatus3 in linea:
            vcuentatotal = vcuentatotal+1

            #We can use replace() to remove all the whitespaces from the string. This function will remove whitespaces between words too.
            linea = (linea.replace(",", ""))    #Se elimina la coma del campo Cantidad
            linea = ",".join(linea.split())     #Se eliminan los espacios en blanco duplicados y se sustituyen con una coma como delimitador
            columnas=linea.split(',')           #Se pasa la cadena a una variable tipo lista

            if 'PMX' in columnas[len(columnas)-6]:
                columnas.append('LOCAL')
            else:
                columnas.append('FORANEO')
                
            bls=float(columnas[len(columnas)-5]) / 159
            columnas.append(str(bls))

            # La función len() devuelve la longitud de la lista (su cantidad de elementos)
            union=columnas[0:6] + columnas[len(columnas)-12:len(columnas)]
            #print(union)
            #print(len(union))
            # usar el método str.join() para convertir una lista que tiene elementos de tipo datos str a una cadena

            linea=",".join(union)+'\n'
            #linea=(linea, end='')
            file.writelines(linea)
            linea = archivo.readline()

file.close()
columnasdatos=['Viaje', 'Pedido', 'Orden', 'Cons', 'Sal', 'Cliente', 'Dest', 'Producto', 'Pres' ,'MT', 'Vehículo', 'Tonel', 'Cantidad', 'Tiempo', 'Estatus', 'Turno', 'Reparto', 'BLS']

df = pd.read_csv('copy.txt', header=None, names=columnasdatos)

#print(df)

print("\nTOTAL VIAJES PROGRAMADOS: ", vcuentatotal)
df.columns
print("PRODUCTOS PROGRAMADOS: ", pd.unique(df['Producto'].sort_values(ascending=True)))

#print(df.dtypes)   muestra los tipos de datos de columnas

# Datos agrupados por Producto
grouped_data = df.groupby('Producto')

#print(grouped_data.describe())     # Estadísticas para todas las columnas numéricas por Producto
print("\nTOTAL VIAJES PROGRAMADOS POR PRODUCTO: ")
print(grouped_data['Viaje'].count())

# Regresa la media de cada columna numérica por viaje
#print(grouped_data.mean())

#grouped_data2 = df.groupby(['Producto', 'Cliente', 'Dest'])
# Estadísticas para todas las columnas numéricas por Producto
#print(grouped_data2['Dest'].count())
# Cuenta el número de viajes cliente-destino por Producto
#clientedest_counts2 = df.groupby(['Producto', 'Cliente', 'Dest']).count()
#print("TOTAL VIAJES POR CLIENTE-DESTINO: ")
#print(clientedest_counts2.groupby('Producto')['Viaje'].count())

grouped_data2 = df.groupby(['Reparto', 'Producto'])
# Estadísticas para todas las columnas numéricas por Producto
print("\nTOTAL VIAJES PROGRAMADOS REPARTO/PRODUCTO: ")
print(grouped_data2['Viaje'].count())






grouped_data5 = df.groupby(['Reparto','Producto', 'Cliente', 'Dest']).agg({'Viaje':'count', 'Cliente':'nunique', 'Cantidad':'sum','BLS':'sum', })
# Estadísticas para todas las columnas numéricas por Producto
print("\nTOTAL VIAJES PROGRAMADOS REPARTO/PRODUCTO: ")
print(grouped_data5.groupby(['Reparto','Producto']).sum())

grouped_data7 = df.groupby(['Estatus','Reparto','Producto', 'Cliente', 'Dest']).agg({'Viaje':'count', 'Cliente':'nunique', 'Cantidad':'sum','BLS':'sum', })
# Estadísticas para todas las columnas numéricas por Producto
print("\nESTATUS VIAJES PROGRAMADOS REPARTO-PRODUCTO/CLIENTE-DESTINO: ")
print(grouped_data7.groupby(['Estatus', 'Reparto','Producto']).sum())

grouped_data4 = df.groupby(['Estatus','Reparto','Producto', 'Cliente', 'Dest']).agg({'Viaje':'count', 'Cliente':'nunique', 'Cantidad':'sum','BLS':'sum', })
# Estadísticas para todas las columnas numéricas por Producto
print("\nESTATUS VIAJES PROGRAMADOS REPARTO-PRODUCTO/CLIENTE-DESTINO:cccxxx ")
grouped_data4.groupby(['Estatus', 'Reparto','Producto']).sum()

grouped_data4.pivot(index='Estatus', columns=['Reparto'], values=['Viaje', 'Cliente', 'Cantidad', 'BLS'])

