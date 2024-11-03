from diabetesModel import diabetesModel
from diabetesInference import diabetesInference
from quiz import Quiz

if __name__ == '__main__':

    # Parte INICIAL DEL DIAGNÓSTICO (basado en síntomas y factores de riesgo)
    quiz = Quiz()
    res = quiz.do_initial_quiz()
    # print(res)


    # Crear MODELO INICIAL 
    model = diabetesModel().create_initial_model()

    evidence = res.values()

    inference = diabetesInference(model)
    inference.inference_example(evidence)
    

