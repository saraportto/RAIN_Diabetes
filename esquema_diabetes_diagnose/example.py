### GENERAR DATASET FICTICIO DE EJEMPLO

# Imports
import pandas as pd # Para trabajar con dataframe y csv
import numpy as np # Para generar aleatorios

# Semilla aleatoria (para que sean siempre los mismos resultados)
np.random.seed(42)

def create_example(instances, filename):
    # Crear dataframe de pandas, con los parámetros
    # el array de números son las opciones del parámetro 
    # size es el número de muestras
    data = pd.DataFrame({
        'Edad': np.random.choice([0, 1, 2], size=instances),  # 0: joven, 1: adulto, 2: mayor
        'NivelGlucosa': np.random.choice([0, 1], size=instances),  # 0: bajo, 1: alto
        'IMC': np.random.choice([0, 1, 2], size=instances) #,  # 0: bajo, 1: normal, 2: alto
        #'Diabetes': np.random.choice([0, 1], size=10000000)  # 0: no, 1: sí
    })

    # Pasar el dataframe de pandas a CSV
    data.to_csv(filename, index=False)

    # Imprimir mensaje de comprobación
    print("Dataset de ejemplo generado y guardado como 'data.csv'.")