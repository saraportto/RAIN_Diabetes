from diabetesModel import diabetesModel
from diabetesInference import diabetesInference
import pandas as pd 

if __name__ == '__main__':
    
    ### DESCOMENTAR el filename con el nombre del fichero a utilizar
    #filename = "test/test_normal.csv"
    #filename = "test/test_clinico.csv"
    #filename = "test/pruebas_normal.csv"
    filename = "test/pruebas_clinico.csv"
    filename = "test/pruebita.csv"

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