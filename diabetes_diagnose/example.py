import pandas as pd
import numpy as np

# Generamos un dataset ficticio con variables relacionadas con el diagnóstico de diabetes
np.random.seed(42)  # Para que los resultados sean reproducibles

# Simulamos variables: edad, nivel de glucosa, IMC y diabetes (sí/no)
data = pd.DataFrame({
    'Edad': np.random.choice([0, 1, 2], size=1000),  # 0: joven, 1: adulto, 2: mayor
    'NivelGlucosa': np.random.choice([0, 1], size=1000),  # 0: bajo, 1: alto
    'IMC': np.random.choice([0, 1, 2], size=1000),  # 0: bajo, 1: normal, 2: alto
    'Diabetes': np.random.choice([0, 1], size=1000)  # 0: no, 1: sí
})

# Guardamos el dataset simulado en un archivo CSV
data.to_csv('data.csv', index=False)

print("Dataset de ejemplo generado y guardado como 'data.csv'.")
