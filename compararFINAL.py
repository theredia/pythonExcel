import pandas as pd


#-------------------------------------------
#Importa los ficheros Excel al DataFrame
#-------------------------------------------

df1 = pd.read_excel('1.xlsx')
df2 = pd.read_excel('2.xlsx')

#-------------------------------------------
#A cada Dataframe añade la columna "Fecha"
#-------------------------------------------

for index, row in df1.iterrows():
	df1["Fecha"]=1


for index, row in df2.iterrows():
	df2["Fecha"]=2

#-------------------------------------------
#Imprime número de registros de cada DataFrame
#-------------------------------------------

print ("Número de registros Fecha 1: ",len(df1))
print ("Número de registros Fecha 2: ",len(df2))

#-------------------------------------------
#Imprime el número de registros y el número de columnas de cada DataFrame
#-------------------------------------------

print("Número de registros Fecha 1 + Columnnas: ",df1.shape)
print("Número de registros Fecha 2 + Columnnas: ",df2.shape)

#-------------------------------------------
#Devuelve los registros que no están en la Fecha 1
#-------------------------------------------

print ("Fecha 2---------------------------------")
df3 = df1.append(df2, sort=True)
bool_series = (df3.duplicated(["Operario"]))
data = df3[~bool_series]
noDuplicados = (data.loc[data['Fecha'] > 1])
noDuplicados.to_excel('nuevosFechaFecha2.xlsx', sheet_name='Fecha2', index=False)
print ("Registros que no están en la fecha 1: ",len(noDuplicados))

#-------------------------------------------
#Devuelve los registros que no están en la Fecha 2
#-------------------------------------------

print ("Fecha 1----------------------")
df5 = df2.append(df1, sort=True)
bool_series = (df5.duplicated(["Operario"]))
data = df5[~bool_series]
noDuplicados = (data.loc[data['Fecha'] < 2])
noDuplicados.to_excel('nuevosFechaFecha1.xlsx', sheet_name='Fecha1', index=False)
print ("Registros que no están en la fecha 2: ",len(noDuplicados))

