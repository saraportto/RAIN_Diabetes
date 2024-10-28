import pandas as pd 
from pgmpy.inference import VariableElimination


# OPCIÓN 1: HACER UN EJEMPLO CONCRETO
def inference_example(model, [age, gluc, imc]):
    # Crear el motor de inferencia
    infer = VariableElimination(model)  

    # Proporcionamos evidencia: persona mayor (Edad=2), glucosa alta (NivelGlucosa=1), IMC alto (IMC=2)
    evidence = {'Edad': age, 'NivelGlucosa': gluc, 'IMC': imc}
    resultado = infer.query(variables=['Diabetes'], evidence=evidence)

    print(f"Resultado de la inferencia: {resultado}")


# OPCIÓN 2: LEER DE UN CSV CONCRETO
def inference_csv(model, filename):
    # Crear el motor de inferencia
    infer = VariableElimination(model)  

    data = pd.read_csv(filename)

    for index, row in data.iterrows():
        evidence = {'Edad': row['Edad'], 'NivelGlucosa': row['NivelGlucosa'], 'IMC': row['IMC']}
        resultado = infer.query(variables=['Diabetes'], evidence=evidence)
        
        print(f"Fila {index + 1}: Resultado de la inferencia: {resultado}")
