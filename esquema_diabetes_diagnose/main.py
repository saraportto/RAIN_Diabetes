from diabetes_model import create_model
from inference import inference_example
from example import create_csv, do_quiz


if __name__ == "__main__":

    #create_csv(15, 'data2.csv')

    res = do_quiz()

    model = create_model()

    inference_example(model, [0, 0, 0])