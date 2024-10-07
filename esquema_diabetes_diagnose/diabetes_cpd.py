from pgmpy.factors.discrete import TabularCPD

# Definir las probabilidades condicionales (CPDs)
cpd_edad = TabularCPD(variable='Edad', variable_card=3, values=[[0.3], [0.5], [0.2]])  # Probabilidad de ser joven/adulto/mayor
cpd_glucosa = TabularCPD(variable='NivelGlucosa', variable_card=2, values=[[0.7], [0.3]])
cpd_imc = TabularCPD(variable='IMC', variable_card=3, values=[[0.4], [0.4], [0.2]])

# CPD para la variable Diabetes, con 18 combinaciones de Edad, NivelGlucosa y IMC
cpd_diabetes = TabularCPD(
    variable='Diabetes',
    variable_card=2,
    values=[[0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.8, 0.7, 0.6, 
             0.9, 0.6, 0.3, 0.5, 0.4, 0.7, 0.5, 0.2, 0.3],  # Probabilidades para Diabetes=0

            [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.2, 0.3, 0.4,
             0.1, 0.4, 0.7, 0.5, 0.6, 0.3, 0.5, 0.8, 0.7]],  # Probabilidades para Diabetes=1
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
