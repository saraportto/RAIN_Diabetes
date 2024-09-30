from pgmpy.inference import VariableElimination

# Cargamos el motor de inferencia
infer = VariableElimination(model)

# Supongamos que queremos predecir si una persona mayor (Edad=2), con glucosa alta (NivelGlucosa=1) y IMC alto (IMC=2) tiene diabetes
evidence = {'Edad': 2, 'NivelGlucosa': 1, 'IMC': 2}
resultado = infer.map_query(variables=['Diabetes'], evidence=evidence)

print(f"Resultado de la inferencia para los datos de prueba: {resultado}")
