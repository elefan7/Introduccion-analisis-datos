import pandas as pd
from datasets import load_dataset

# Cargar el conjunto de datos
dataset = load_dataset("mstz/heart_failure")

# Crear un DataFrame a partir del conjunto de datos
df = pd.DataFrame(dataset['train'])

# Separar el DataFrame en dos según la condición 'is_dead'
df_dead = df[df['is_dead'] == 1]
df_alive = df[df['is_dead'] == 0]

# Mostrar los DataFrames resultantes
print("DataFrame con personas que fallecieron:")
print(df_dead)
print("\nDataFrame con personas que no fallecieron:")
print(df_alive)

# Calcular los promedios de las edades de cada dataset e imprimir
prom_age_dead = round(df_dead['age'].mean(), 1)
prom_age_alive = round(df_alive['age'].mean(), 1)

print("\nPromedio edad de personas fallecidas:", prom_age_dead)
print("Promedio de edades para personas que no fallecieron:", prom_age_alive)
