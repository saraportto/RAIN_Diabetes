from pgmpy.inference import VariableElimination
import pandas as pd


class diabetesInference:
   
   # La clase inferencia guarda el modeo y la VariableElimination en base al modelo
    def __init__(self, model):
        self.model = model
        self.inference = VariableElimination(model)


    # Inferencia cuando se reciben respuestas de un QUIZ
    def inference_example(self, evidence_vals: list):
        
        evidence_keys = [
            'age', 'bmi', 'pancreas_diseases','family_history', 
            'urinate_freq', 'thirst', 'fatigue', 'hunger', 'weight_loss', 'sympt_diseases'
        ]

        # Añadir CLAVES CLÍNICAS si se recibe un quiz clínico
        if len(evidence_vals) > 10:
            evidence_keys += ['glucose', 'blood_pressure']
        
        # Diccionario con claves y valores de las respuestas
        evidence = dict(zip(evidence_keys, evidence_vals))

        #print("Evidencia para inferencia:", evidence)

        ### INFERENCIA ###
        resultado = self.inference.query(variables=['diabetes'], evidence=evidence)
        
        # Probabilidad de TENER DIABETES
        return resultado.values[1]
    

    # Inferencia cuando se reciben respuestas de un CSV
    def inference_csv(self, filename: str, is_clinical: bool):

        # Cargar el archivo CSV
        data = pd.read_csv(filename)

        # Lista que almacena probabilidades de diabetes
        diabetes_probabilities = []   
        
        # Por cada fila, sacar la evidence
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

            # Añadir datos clínicos si el csv es clínico
            if is_clinical:
                evidence['glucose'] = row['glucose']
                evidence['blood_pressure'] = row['blood_pressure']

            ### INFERENCIA ###
            resultado = self.inference.query(variables=['diabetes'], evidence=evidence)
            diabetes_probability = resultado.values[1]  # Probabilidad de tener diabetes

            #print(f"Fila {index + 1}: Probabilidad de diabetes: {diabetes_probability}")

            # Añadir prob a la lista
            diabetes_probabilities.append(diabetes_probability)

        ## GUARDAR EN NUEVO CSV
        # Añadir columna diabetes con la lista de probabilidades
        data['diabetes'] = diabetes_probabilities

        new_filename = filename.replace('.csv', '_solved.csv')

        data.to_csv(new_filename, index=False)

        print(f"\n\nArchivo con resultados guardado como: {new_filename}\n")

        return diabetes_probabilities