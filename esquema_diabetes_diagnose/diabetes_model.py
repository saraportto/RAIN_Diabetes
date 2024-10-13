### CREACIÓN DEL MODELO

# Imports
from pgmpy.models import BayesianNetwork 
from diabetes_cpd import cpd_edad, cpd_glucosa, cpd_imc, cpd_diabetes  # Importamos las CPDs


def create_model():
    # Define el modelo, con los arcos entre los nodos en la red bayesiana
    model = BayesianNetwork([('Edad', 'Diabetes'),
                            ('NivelGlucosa', 'Diabetes'),
                            ('IMC', 'Diabetes')])

    # Añade las CPDs al modelo
    model.add_cpds(cpd_edad, cpd_glucosa, cpd_imc, cpd_diabetes)

    # Verifica si el modelo es válido
    assert model.check_model()

    # Imprimir mensaje de comprobación
    print("Modelo de diabetes creado y CPDs añadidas correctamente.")