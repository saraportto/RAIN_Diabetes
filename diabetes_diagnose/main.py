from diabetesModel import diabetesModel
from diabetesInference import diabetesInference
from quiz import Quiz

import time

if __name__ == '__main__':

    ### Parte INICIAL del diagnóstico (basado en síntomas y factores de riesgo) ###
    # QUIZ inicial
    quiz = Quiz()
    res = quiz.do_initial_quiz()
    #print(res)

    # Crear MODELO INICIAL 
    model = diabetesModel().create_initial_model()

    # Hacer la INFERENCIA INICIAL con el EJEMPLO del quiz
    evidence = res.values()
    inference = diabetesInference(model)
    prob_diabetes_inicial = inference.inference_example(evidence)

    print("\n\n-----------------------------------")
    print("PROBABILIDAD DE TENER DIABETES:\n", prob_diabetes_inicial)
    print("-----------------------------------")

    ### SEGUNDA PARTE del diagnóstico (añadiendo test clínico) ###
    if prob_diabetes_inicial > 0.3:

        time.sleep(1)
        print("\nLos resultados del cuestionario que hay una probabilidad considerable de tener diabetes.")
        print("Es necesario hacer un examen médico.\n")

        time.sleep(0.2)
        print("Recogiendo muestras", end="")

        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        # QUIZ clínico
        clinical_res = quiz.do_clinical_quiz(res)
        #print("Resultados del quiz clínico:", clinical_res)

        # Crear el MODELO CLÍNICO 
        clinical_model = diabetesModel().create_clinical_model()

        # COMBINAR evidencia inicial con la clínica
        clinical_evidence = clinical_res.values()
        complete_evidence = list(evidence) + list(clinical_evidence)

        # INFERENCIA con el modelo clínico
        clinical_inference = diabetesInference(clinical_model)
        prob_diabetes_final = clinical_inference.inference_example(complete_evidence)
        
        print("\n\n-----------------------------------")
        print("PROBABILIDAD DE TENER DIABETES\n(con el test clínico):\n", prob_diabetes_final)    
        print("-----------------------------------")

    else: # Si la probabilidad de tener diabetes no es significativa
        print ("\nLa probabilidad de que tenga diabetes es baja, no es necesario hacer ningún test clínico.")