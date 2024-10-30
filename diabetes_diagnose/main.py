# from diabetesModel import diabetesModel
# from diabetesInference import diabetesInference
from quiz import Quiz

if __name__ == '__main__':

    quiz = Quiz()
    res = quiz.do_initial_quiz()

    print(res)


    '''
    evidence = res.values()

    model = diabetesModel.create_initial_model

    inference = diabetesInference(model)
    '''
    

