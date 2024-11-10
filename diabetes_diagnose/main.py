from diabetesModel import diabetesModel
from diabetesInference import diabetesInference
from quiz import Quiz

if __name__ == '__main__':

    # Parte INICIAL DEL DIAGNÓSTICO (basado en síntomas y factores de riesgo)
    quiz = Quiz()
    res = quiz.do_initial_quiz()
    print(res)

    # Crear MODELO INICIAL 
    model = diabetesModel().create_initial_model()

    evidence = res.values()

    inference = diabetesInference(model)
    prob_diabetes_inicial = inference.inference_example(evidence)

    if prob_diabetes_inicial > 0.5:
        clinical_res = quiz.do_clinical_quiz(res)
        print("Resultados del quiz clínico:", clinical_res)

        # Crear el modelo clínico 
        clinical_model = diabetesModel().create_clinical_model()

        # Combinar evidencia inicial con la clínica. Evidence se convierte en una lista paea que se puede juntar con clinical_res
        complete_evidence = clinical_res.values()

        # Inferencia con el modelo clínico
        clinical_inference = diabetesInference(clinical_model)
        prob_diabetes_final = clinical_inference.inference_example(complete_evidence)
        print("Probabilidad de diabetes después del test clínico:", prob_diabetes_final)


    