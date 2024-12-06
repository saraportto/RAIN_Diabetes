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

        # Columnas según el tipo de csv
        base_columns = [
            'age', 'bmi', 'pancreas_diseases', 'family_history', 
            'urinate_freq', 'thirst', 'fatigue', 'hunger', 
            'weight_loss', 'sympt_diseases'
        ]

        clinical_columns = ['glucose', 'blood_pressure'] if is_clinical else []

        required_columns = base_columns + clinical_columns

        
        # Por cada fila, sacar la evidence
        for index, row in data.iterrows():

            # Evidencia
            evidence = {col: row[col] for col in required_columns}

            ### INFERENCIA ###
            resultado = self.inference.query(variables=['diabetes'], evidence=evidence)
            diabetes_probability = resultado.values[1]  # Probabilidad de tener diabetes

            #print(f"Fila {index + 1}: Probabilidad de diabetes: {diabetes_probability}")

            # Añadir prob a la lista
            diabetes_probabilities.append(f"{diabetes_probability*100:.4f} %")


        ## GUARDAR EN NUEVO CSV
        # Añadir columna diabetes con la lista de probabilidades
        data['diabetes_prob'] = diabetes_probabilities

        # Añadir columna DIABETES con SI/NO según la probabilidad
        if is_clinical:
            data['DIABETES'] = data['diabetes_prob'].apply(lambda x: 'SI' if float(x.replace(' %', '')) > 50 else 'NO')
        else:
            data['DIABETES'] = data['diabetes_prob'].apply(lambda x: 'SI' if float(x.replace(' %', '')) > 30 else 'NO')

        new_filename = filename.replace('.csv', '_solved.csv')

        data.to_csv(new_filename, index=False)

        print(f"\n\nArchivo con resultados guardado como: {new_filename}\n")

        return diabetes_probabilities