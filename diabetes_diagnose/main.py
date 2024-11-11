from diabetesModel import diabetesModel
from diabetesInference import diabetesInference
from quiz import Quiz

import time

if __name__ == '__main__':

    # Parte INICIAL DEL DIAGNÓSTICO (basado en síntomas y factores de riesgo)
    quiz = Quiz()
    res = quiz.do_initial_quiz()
    #print(res)

    # Crear MODELO INICIAL 
    model = diabetesModel().create_initial_model()
    evidence = res.values()

    # Hacer la INFERENCIA INICIAL con el EJEMPLO del quiz
    inference = diabetesInference(model)
    prob_diabetes_inicial = inference.inference_example(evidence)

    print("\n\n---------------------------")
    print("PROBABILIDAD DE TENER DIABETES: ", prob_diabetes_inicial)
    print("---------------------------")

    if prob_diabetes_inicial > 0.3:
        time.sleep(1)
        print("\nLos resultados del cuestionario que hay una probabilidad considerable de tener diabetes.")
        print("Es necesario hacer un examen médico.\n")

        # Espera de 0,2 segundos
        time.sleep(0.2)
        print("Recogiendo muestras", end="")

        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        clinical_res = quiz.do_clinical_quiz(res)
        #print("Resultados del quiz clínico:", clinical_res)

        # Crear el modelo clínico 
        clinical_model = diabetesModel().create_clinical_model()

        # Combinar evidencia inicial con la clínica. Evidence se convierte en una lista paea que se puede juntar con clinical_res
        complete_evidence = list(res.values()) + list(clinical_res.values())

        # Inferencia con el modelo clínico
        clinical_inference = diabetesInference(clinical_model)
        prob_diabetes_final = clinical_inference.inference_example(complete_evidence)
        print("Probabilidad de diabetes después del test clínico:", prob_diabetes_final)    