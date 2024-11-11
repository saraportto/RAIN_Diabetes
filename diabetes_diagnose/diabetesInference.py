from pgmpy.inference import VariableElimination
import pandas as pd


class diabetesInference:
   
    def __init__(self, model):
        self.model = model
        self.inference = VariableElimination(model)


    # Inferencia cuando se reciben respuestas de un quiz
    def inference_example(self, evidence_vals: list):
        
        evidence_keys = [
            'age', 'bmi', 'pancreas_diseases','family_history', 
            'urinate_freq', 'thirst', 'fatigue', 'hunger', 'weight_loss', 'sympt_diseases'
        ]

        # Añadir claves clínicas cuando se reciba quiz clínico
        if len(evidence_vals) > 10:
            evidence_keys += ['glucose', 'blood_pressure']
        
        # Combinar respuestas y claves
        evidence = dict(zip(evidence_keys, evidence_vals))

        #print("Evidencia para inferencia:", evidence)

        ### INFERENCIA ###
        resultado = self.inference.query(variables=['diabetes'], evidence=evidence)
        
        # Probabilidad de TENER DIABETES
        return resultado.values[1]
    

    def inference_csv(self, filename: str, is_clinical: bool):
        # Cargar el archivo CSV
        data = pd.read_csv(filename)

        # Crear una lista para almacenar las probabilidades de diabetes
        diabetes_probabilities = []   
        
        # Iterar sobre cada fila del DataFrame
        for index, row in data.iterrows():
            evidence = {
                'age': row['age'], 
                'bmi': row['bmi'], 
                'pancreas_diseases': row['pancreas_diseases'],
                'family_history': row['family_history'], 
                'urinate_freq': row['urinate_freq'], 
                'thirst': row['thirst'], 
                'fatigue': row['fatigue'], 
                'hunger': row['hunger'], 
                'weight_loss': row['weight_loss'], 
                'sympt_diseases': row['sympt_diseases']
            }

            # Añadir datos clínicos si están presentes
            if is_clinical:
                evidence['glucose'] = row['glucose']
                evidence['blood_pressure'] = row['blood_pressure']

            # Realizar la inferencia
            resultado = self.inference.query(variables=['diabetes'], evidence=evidence)
            diabetes_probability = resultado.values[1]  # Probabilidad de tener diabetes

            # Imprimir el resultado de la inferencia para depuración
            print(f"Fila {index + 1}: Probabilidad de diabetes: {diabetes_probability}")

            # Añadir la probabilidad de diabetes a la lista
            diabetes_probabilities.append(diabetes_probability)

        # Añadir la columna de probabilidades al DataFrame original
        data['diabetes'] = diabetes_probabilities

        # Generar el nombre del nuevo archivo CSV
        new_filename = filename.replace('.csv', '_solved.csv')

        # Guardar el DataFrame con la nueva columna de probabilidades en un archivo nuevo
        data.to_csv(new_filename, index=False)

        print(f"\n\nArchivo con resultados guardado como: {new_filename}\n")