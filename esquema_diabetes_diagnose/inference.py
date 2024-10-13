import pandas as pd 
from pgmpy.inference import VariableElimination
from diabetes_model import model  # Importamos el modelo desde diabetes_model.py


# OPCIÓN 1: HACER UN EJEMPLO CONCRETO
def inference_example(age, gluc, imc):
    # Crear el motor de inferencia
    infer = VariableElimination(model)  

    # Proporcionamos evidencia: persona mayor (Edad=2), glucosa alta (NivelGlucosa=1), IMC alto (IMC=2)
    evidence = {'Edad': age, 'NivelGlucosa': age, 'IMC': age}
    resultado = infer.query(variables=['Diabetes'], evidence=evidence)

    print(f"Resultado de la inferencia: {resultado}")


# OPCIÓN 2: LEER DE UN CSV CONCRETO
def inference_csv(filename):
    # Crear el motor de inferencia
    infer = VariableElimination(model)  

    data = pd.read_csv(filename)

    for index, row in data.iterrows():
        evidence = {'Edad': row['Edad'], 'NivelGlucosa': row['NivelGlucosa'], 'IMC': row['IMC']}
        resultado = infer.query(variables=['Diabetes'], evidence=evidence)
        
        print(f"Fila {index + 1}: Resultado de la inferencia: {resultado}")
