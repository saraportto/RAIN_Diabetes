from pgmpy import VariableElimination

class diabetesInference:
   
    def __init__(self, model, inference):
        self.model = model
        self.inference = inference

    def create_initial_model(self, evidence_vals: list):
        pass

    def create_clinical_model(self, filename: str):
        pass