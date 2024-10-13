### CREACIÓN DEL MODELO

# Imports
from pgmpy.models import BayesianNetwork 
from pgmpy.factors.discrete import TabularCPD


# Probabilidades condicionales (CPDs), para cada parámetro relacionado con la diabetes
# Qué probabilidad hay de que alguien sea...
cpd_edad = TabularCPD(variable='Edad', variable_card=3, values=[[0.3], [0.5], [0.2]])  # Probabilidad de ser joven/adulto/mayor
cpd_glucosa = TabularCPD(variable='NivelGlucosa', variable_card=2, values=[[0.7], [0.3]]) # Probabilidad de tener glucosa baja/alta
cpd_imc = TabularCPD(variable='IMC', variable_card=3, values=[[0.4], [0.4], [0.2]]) # Probabilidad de tener IMC bajo/normal/alto


# CPD para la variable Diabetes, con 18 (combinaciones de Edad, NivelGlucosa y IMC, 3 x 2 x 3)
# Qué probabilidad hay de que alguien tenga diabetes, dependiendo de los parámetros (edad, glucosa e imc)
# Pesos (relación parámetros con diabetes)
cpd_diabetes = TabularCPD(
    variable='Diabetes',
    variable_card=2,
    values=[[0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 
            0.8, 0.7, 0.6, 0.9, 0.6, 0.3, 
            0.5, 0.4, 0.7, 0.5, 0.2, 0.3],  # Probabilidades para Diabetes=0

            [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 
            0.2, 0.3, 0.4, 0.1, 0.4, 0.7, 
            0.5, 0.6, 0.3, 0.5, 0.8, 0.7]],  # Probabilidades para Diabetes=1

    evidence=['Edad', 'NivelGlucosa', 'IMC'], 
    evidence_card=[3, 2, 3]  # Número de estados de cada evidencia
)
    

'''
Ejemplo de interpretación:
Para la primera columna 
(donde Edad = Joven, NivelGlucosa = Bajo, IMC = Bajo), 
las probabilidades son:

0.9 para Diabetes = No.
0.1 para Diabetes = Sí.
'''


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
    
    return model