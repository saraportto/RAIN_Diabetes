from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Definir la estructura del modelo
model = BayesianNetwork([('Edad', 'Diabetes'),
                         ('NivelGlucosa', 'Diabetes'),
                         ('IMC', 'Diabetes')])

# Definir las probabilidades condicionales (CPDs)
cpd_edad = TabularCPD(variable='Edad', variable_card=3, values=[[0.3], [0.5], [0.2]])
cpd_glucosa = TabularCPD(variable='NivelGlucosa', variable_card=2, values=[[0.7], [0.3]])
cpd_imc = TabularCPD(variable='IMC', variable_card=3, values=[[0.4], [0.4], [0.2]])

# CPD para la variable Diabetes, con 18 combinaciones de Edad, NivelGlucosa y IMC
cpd_diabetes = TabularCPD(variable='Diabetes', variable_card=2,
                          values=[[0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.8, 0.7, 0.6, 
                                   0.9, 0.6, 0.3, 0.5, 0.4, 0.7, 0.5, 0.2, 0.3],
                                  [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.2, 0.3, 0.4,
                                   0.1, 0.4, 0.7, 0.5, 0.6, 0.3, 0.5, 0.8, 0.7]],
                          evidence=['Edad', 'NivelGlucosa', 'IMC'],
                          evidence_card=[3, 2, 3])

# Añadir los CPDs al modelo
model.add_cpds(cpd_edad, cpd_glucosa, cpd_imc, cpd_diabetes)

# Verificar si el modelo es válido
assert model.check_model()

print("Modelo de diabetes creado correctamente.")
