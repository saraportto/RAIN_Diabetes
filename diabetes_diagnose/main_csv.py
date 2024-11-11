from diabetesModel import diabetesModel
from diabetesInference import diabetesInference
import pandas as pd 

if __name__ == '__main__':
    
    #filename = "test/test_normal.csv"
    filename = "test/test_clinico.csv"

    data = pd.read_csv(filename)

    # Verifica si es un archivo clínico o normal
    is_clinical = 'glucose' in data.columns and 'blood_pressure' in data.columns

    if is_clinical:
        model = diabetesModel().create_clinical_model() 

    else:
        model = diabetesModel().create_initial_model()

    infer = diabetesInference(model)
    infer.inference_csv(filename, is_clinical)