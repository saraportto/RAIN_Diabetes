from pgmpy.models import BayesianNetwork
from diabetes_cpd import cpd_edad, cpd_glucosa, cpd_imc, cpd_diabetes  # Importamos las CPDs

# Definir la estructura del modelo
model = BayesianNetwork([('Edad', 'Diabetes'),
                         ('NivelGlucosa', 'Diabetes'),
                         ('IMC', 'Diabetes')])

# Añadir las CPDs al modelo
model.add_cpds(cpd_edad, cpd_glucosa, cpd_imc, cpd_diabetes)

# Verificar si el modelo es válido
assert model.check_model()

print("Modelo de diabetes creado y CPDs añadidas correctamente.")
