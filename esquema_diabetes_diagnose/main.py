from diabetes_model import create_model
from inference import inference_example
from example import create_csv

if __name__ == "__main__":
    create_csv(15, 'data2.csv')
    model = create_model()

    inference_example(model, 0, 0, 0)