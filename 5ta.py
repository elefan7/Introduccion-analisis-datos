import pandas as pd

def procesar_datos(df):
    # Verificar que no existan valores faltantes
    valores_faltantes = df.isnull().sum()
    print("Valores faltantes:\n", valores_faltantes)

    # Verificar que no existan filas repetidas
    filas_duplicadas = df.duplicated().sum()
    print("Número de filas duplicadas: ", filas_duplicadas)

    # Verificar si existen valores atípicos y eliminarlos
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    filtro_atipico = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
    sin_atipicos = df[~filtro_atipico]
    
    print("\nInformación antes de eliminar valores atípicos:")
    print(df.info())
    
    print("\nInformación después de eliminar valores atípicos:")
    print(sin_atipicos.info())

    # Crear una columna que categorice por edades
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescentes', 'Joven adulto', 'Adulto', 'Adulto mayor']
    df['Categoría de Edad'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

    print(df)
    
    # Guardar el resultado como CSV
    df.to_csv('datos_procesados.csv', index=False)

# Leer el DataFrame desde el archivo CSV
df = pd.read_csv("introduccion-analisis-datos.csv")

# Procesar los datos usando la función
procesar_datos(df)

