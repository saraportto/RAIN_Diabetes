#### NO DEFINITIVO ###

from pgmpy.models import GaussianNetwork
from pgmpy.factors.continuous import LinearGaussianCPD

# Crear un modelo gaussiano
model = GaussianNetwork([('Edad', 'Diabetes'), ('NivelGlucosa', 'Diabetes'), ('IMC', 'Diabetes')])

# Definir CPDs para las variables continuas
cpd_edad = LinearGaussianCPD('Edad', mean=40, variance=10)  # Suponiendo que la edad tiene una media de 40 años y una varianza de 10

# Definir CPDs para las otras variables (NivelGlucosa y IMC)
cpd_glucosa = LinearGaussianCPD('NivelGlucosa', mean=100, variance=15)  # Suponiendo que el nivel de glucosa es continuo
cpd_imc = LinearGaussianCPD('IMC', mean=25, variance=5)  # Suponiendo que el IMC es continuo

# Añadir los CPDs al modelo
model.add_cpds(cpd_edad, cpd_glucosa, cpd_imc)

# Definir las dependencias con la variable de salida (Diabetes)
# Esto requiere modelar la relación entre las variables continuas y discretas
