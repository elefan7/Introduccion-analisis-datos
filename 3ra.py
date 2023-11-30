import pandas as pd
from datasets import load_dataset
# Cargar el conjunto de datos

dataset = load_dataset("mstz/heart_failure")

# Crear un DataFrame a partir del conjunto de datos
df = pd.DataFrame(dataset['train'])

# Mostrar los tipos de datos en cada columna
print("Tipos de datos en cada columna:")
print(df.dtypes)

# Verificar si hay columnas numéricas en formato de cadena
numeric_columns_as_string = [col for col, dtype in df.dtypes.items() if dtype == 'object']
if numeric_columns_as_string:
    print("\n¡Advertencia! Las siguientes columnas numéricas están en formato de cadena:")
    print(numeric_columns_as_string)
else:
    print("\nTodos los tipos de datos son correctos.")
    

print("\n" + "=" * 50 + "\n")


#Calcular la cantidad de hombres fumadores vs mujeres fumadoras
query = ['is_male', 'is_smoker']
df_filtrado = df[query]

#Agrupar y contar
res = df_filtrado.groupby(['is_male', 'is_smoker']).size().unstack(fill_value=0)

print("Cantidad de hombre y mujeres fumador@s:", res)