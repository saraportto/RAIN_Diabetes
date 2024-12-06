from diabetesModel import diabetesModel
from diabetesInference import diabetesInference
import pandas as pd 

if __name__ == '__main__':
    
    ### DESCOMENTAR el filename con el nombre del fichero a utilizar
    #filename = 'test/normal.csv'
    filename = 'test/clinico.csv'
    #filename = 'test/z_more_normal.csv'
    #filename = 'test/z_more_clinical.csv'

    # LEER datos del CSV
    data = pd.read_csv(filename)

    # Crear MODELO, sabiendo si es clínico o no
    is_clinical = 'glucose' in data.columns and 'blood_pressure' in data.columns

    if is_clinical:
        model = diabetesModel().create_clinical_model() 

    else:
        model = diabetesModel().create_initial_model()

    # Hacer INFERENCIA
    infer = diabetesInference(model)
    infer.inference_csv(filename, is_clinical)