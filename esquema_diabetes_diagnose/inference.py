from pgmpy.inference import VariableElimination
from diabetes_model import model  # Importamos el modelo desde diabetes_model.py

# Crear el motor de inferencia
infer = VariableElimination(model)

# Proporcionamos evidencia: persona mayor (Edad=2), glucosa alta (NivelGlucosa=1), IMC alto (IMC=2)
evidence = {'Edad': 2, 'NivelGlucosa': 1, 'IMC': 2}
resultado = infer.map_query(variables=['Diabetes'], evidence=evidence)

print(f"Resultado de la inferencia: {resultado}")
