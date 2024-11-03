from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
import pandas as pd

class diabetesModel:
    
    def __init__(self):
        pass
    

    # Modelo inicial, en base a Red Bayesiana 1
    def create_initial_model(self):
        ### MODELO VACÍO ###
        model = BayesianNetwork()

        ### Añadir NODOS al modelo ###
        nodes = [
            'sex', 'age', 'bmi', 'drugs', 'pancreas_diseases', 'pancreas_injury', 'pregnancies', 'family_history', 
            'diabetes', 
            'urinate_freq', 'thirst', 'fatigue', 'hunger', 'weight_loss', 'sympt_diseases'
        ]
        model.add_nodes_from(nodes)

        ### Añadir ARCOS al modelo ###
        edges = [
            ('sex', 'diabetes'), 
            ('age', 'diabetes'), 
            ('bmi', 'diabetes'), 
            ('drugs', 'diabetes'), 
            ('pancreas_diseases', 'diabetes'), 
            ('pancreas_injury', 'diabetes'),
            ('pregnancies', 'diabetes'), 
            ('family_history', 'diabetes'), 
            ('diabetes', 'urinate_freq'), 
            ('diabetes', 'thirst'), 
            ('diabetes', 'fatigue'), 
            ('diabetes', 'hunger'), 
            ('diabetes', 'weight_loss'), 
            ('diabetes', 'sympt_diseases')
        ]
        model.add_edges_from(edges)

        ### Añadir CPDs al modelo###
        # Probabilidades a priori de FACTORES DE RIESGO
        cpd_sex = TabularCPD(variable='sex', variable_card=2, values=[[0.5], [0.5]])
        cpd_age = TabularCPD(variable='age', variable_card=4, values=[[0.25], [0.25], [0.25], [0.25]])
        cpd_bmi = TabularCPD(variable='bmi', variable_card=3, values=[[0.33], [0.33], [0.34]])
        cpd_drugs = TabularCPD(variable='drugs', variable_card=2, values=[[0.8], [0.2]])
        cpd_pancreas_diseases = TabularCPD(variable='pancreas_diseases', variable_card=2, values=[[0.9], [0.1]])
        cpd_pancreas_injury = TabularCPD(variable='pancreas_injury', variable_card=2, values=[[0.95], [0.05]])
        cpd_pregnancies = TabularCPD(variable='pregnancies', variable_card=2, values=[[0.7], [0.3]])
        cpd_family_history = TabularCPD(variable='family_history', variable_card=2, values=[[0.6], [0.4]])

        # Leer el archivo CSV para las probabilidades de diabetes
        df = pd.read_csv("diabetes_probabilities.csv")

        # CPD para DIABETES (con el CSV)
        cpd_diabetes = TabularCPD(
            variable='diabetes', 
            variable_card=2,
            values=df[['prob_diabetes_0', 'prob_diabetes_1']].values.T.tolist(),
            evidence=['sex', 'age', 'bmi', 'drugs', 'pancreas_diseases', 'pancreas_injury', 'pregnancies', 'family_history'],
            evidence_card=[2, 4, 3, 2, 2, 2, 2, 2]
        )

        # CPD para SÍNTOMAS
        cpd_urinate_freq = TabularCPD(
            variable='urinate_freq', 
            variable_card=3, 
            values=[
                [0.6, 0.2],  # P(urinate_freq=0 | diabetes=0) y P(urinate_freq=0 | diabetes=1)
                [0.3, 0.3],  # P(urinate_freq=1 | diabetes=0) y P(urinate_freq=1 | diabetes=1)
                [0.1, 0.5]   # P(urinate_freq=2 | diabetes=0) y P(urinate_freq=2 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_thirst = TabularCPD(
            variable='thirst', 
            variable_card=3, 
            values=[
                [0.7, 0.3],  
                [0.2, 0.4],  
                [0.1, 0.3]   
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_fatigue = TabularCPD(
            variable='fatigue', 
            variable_card=3, 
            values=[
                [0.5, 0.2],  
                [0.3, 0.3],  
                [0.2, 0.5]   
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_hunger = TabularCPD(
            variable='hunger', 
            variable_card=3, 
            values=[
                [0.6, 0.3],  
                [0.3, 0.4],  
                [0.1, 0.3]   
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_weight_loss = TabularCPD(
            variable='weight_loss', 
            variable_card=2, 
            values=[
                [0.8, 0.3],  
                [0.2, 0.7]   
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_sympt_diseases = TabularCPD(
            variable='sympt_diseases', 
            variable_card=2, 
            values=[
                [0.9, 0.4],  
                [0.1, 0.6]   
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        # Añadir CPDS al modelo
        model.add_cpds(
            cpd_sex, cpd_age, cpd_bmi, cpd_drugs, cpd_pancreas_diseases, 
            cpd_pancreas_injury, cpd_pregnancies, cpd_family_history, 
            cpd_diabetes, cpd_urinate_freq, cpd_thirst, cpd_fatigue, 
            cpd_hunger, cpd_weight_loss, cpd_sympt_diseases
        )

        # COMPROBAR MODELO
        assert model.check_model()

        return model


    def create_clinical_model(self):
        pass