from pgmpy.inference import VariableElimination
# import pandas as pd

class diabetesInference:
   
    def __init__(self, model):
        self.model = model
        self.inference = VariableElimination(model)


    # Inferencia cuando se reciben respuestas de un quiz
    def inference_example(self, evidence_vals: list):
        evidence_keys = [
            'sex', 'age', 'bmi', 'drugs', 'pancreas_diseases', 'pancreas_injury', 'pregnancies', 'family_history', 
            'urinate_freq', 'thirst', 'fatigue', 'hunger', 'weight_loss', 'sympt_diseases'
        ]

        # Añadir claves clínicas cuando se reciba quiz clínico
        if len(evidence_vals) > 10:
            evidence_keys += ['glucose', 'blood_pressure']

        # Combinar respuestas y claves
        evidence = dict(zip(evidence_keys, evidence_vals))

        ### INFERENCIA ###
        resultado = self.infer.query(variables=['diabetes'], evidence=evidence)
        
        # Probabilidad de TENER DIABETES
        return resultado.values[1]


    # Inferencia cuando se reciben respuestas de un CSV
    def inference_csv(self, filename: str):
        pass