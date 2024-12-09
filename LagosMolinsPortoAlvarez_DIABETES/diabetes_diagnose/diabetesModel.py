from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
import pandas as pd

class diabetesModel:

    ### MODELO INICIAL, en base a Red Bayesiana 1
    def create_initial_model(self):
        ## MODELO VACÍO ##
        model = BayesianNetwork()

        ### Añadir NODOS al modelo ###
        nodes = [
            'age', 'bmi', 'pancreas_diseases', 'family_history', 
            'diabetes', 
            'urinate_freq', 'thirst', 'fatigue', 'hunger', 'weight_loss', 'sympt_diseases'
        ]
        model.add_nodes_from(nodes)

        ## Añadir ARCOS al modelo ##
        edges = [
            ('age', 'diabetes'), 
            ('bmi', 'diabetes'), 
            ('pancreas_diseases', 'diabetes'), 
            ('family_history', 'diabetes'), 
            ('diabetes', 'urinate_freq'), 
            ('diabetes', 'thirst'), 
            ('diabetes', 'fatigue'), 
            ('diabetes', 'hunger'), 
            ('diabetes', 'weight_loss'), 
            ('diabetes', 'sympt_diseases')
        ]
        model.add_edges_from(edges)


        ## Añadir CPDs al modelo##
        
        # Probabilidades a PRIORI de FACTORES DE RIESGO
        cpd_age = TabularCPD(variable='age', variable_card=2, values=[[0.6], [0.4]])
        cpd_bmi = TabularCPD(variable='bmi', variable_card=3, values=[[0.55], [0.37], [0.08]])
        cpd_pancreas_diseases = TabularCPD(variable='pancreas_diseases', variable_card=2, values=[[0.99], [ 0.01]])
        cpd_family_history = TabularCPD(variable='family_history', variable_card=2, values=[[0.8], [0.2]])

        # CPD para DIABETES (con el CSV con sus probabilidades)
        df = pd.read_csv("diabetes_probabilities.csv")

        cpd_diabetes = TabularCPD(
            variable='diabetes', 
            variable_card=2,
            values=df[['prob_diabetes_0', 'prob_diabetes_1']].values.T.tolist(),
            evidence=['age', 'bmi', 'pancreas_diseases', 'family_history'],
            evidence_card=[2, 3, 2, 2]
        )

        # CPD para SÍNTOMAS
        cpd_urinate_freq = TabularCPD(
            variable='urinate_freq', 
            variable_card=3, 
            values=[
                [0.6, 0.2],  # P(uf=0 | diabetes=0) y P(uf=0 | diabetes=1)
                [0.3, 0.3],  # P(uf=1 | diabetes=0) y P(uf=1 | diabetes=1)
                [0.1, 0.5]   # P(uf=2 | diabetes=0) y P(uf=2 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_thirst = TabularCPD(
            variable='thirst', 
            variable_card=3, 
            values=[
                [0.7, 0.3],   # P(thirst=0 | diabetes=0) y P(thirst=0 | diabetes=1)
                [0.2, 0.4],   # P(thirst=1 | diabetes=0) y P(thirst=1 | diabetes=1)
                [0.1, 0.3]    # P(thirst=2 | diabetes=0) y P(thirst=2 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_fatigue = TabularCPD(
            variable='fatigue', 
            variable_card=3, 
            values=[
                [0.5, 0.2],  # P(fatigue=0 | diabetes=0) y P(fatigue=0 | diabetes=1)
                [0.3, 0.3],  # P(fatigue=1 | diabetes=0) y P(fatigue=1 | diabetes=1)
                [0.2, 0.5]   # P(fatigue=2 | diabetes=0) y P(fatigue=2 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_hunger = TabularCPD(
            variable='hunger', 
            variable_card=3, 
            values=[
                [0.6, 0.3],  # P(hunger=0 | diabetes=0) y P(hunger=0 | diabetes=1)
                [0.3, 0.4],  # P(hunger=1 | diabetes=0) y P(hunger=1 | diabetes=1)
                [0.1, 0.3]   # P(hunger=2 | diabetes=0) y P(hunger=2 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_weight_loss = TabularCPD(
            variable='weight_loss', 
            variable_card=2, 
            values=[
                [0.8, 0.3],  # P(wl=0 | diabetes=0) y P(wl=0 | diabetes=1)
                [0.2, 0.7]   # P(wl=1 | diabetes=0) y P(wl=1 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        cpd_sympt_diseases = TabularCPD(
            variable='sympt_diseases', 
            variable_card=2, 
            values=[
                [0.9, 0.4],  # P(sd=0 | diabetes=0) y P(sd=0 | diabetes=1)
                [0.1, 0.6]   # P(sd=1 | diabetes=0) y P(sd=1 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        # Añadir CPDS al modelo
        model.add_cpds(
            cpd_age, cpd_bmi, cpd_pancreas_diseases, cpd_family_history, 
            cpd_diabetes, 
            cpd_urinate_freq, cpd_thirst, cpd_fatigue, 
            cpd_hunger, cpd_weight_loss, cpd_sympt_diseases
        )

        # Comprobar modelo
        assert model.check_model()

        return model


    ### MODELO INICIAL, en base a Red Bayesiana 2
    def create_clinical_model(self):

        # Red Bayesiana 1 como base para la Red Bayesiana 2
        clinical_model = self.create_initial_model()

        # Añadir los NODS de glucosa y presión arterial
        nodes =['glucose', 'blood_pressure']
        clinical_model.add_nodes_from(nodes)

        # Añadir ARCOS de quiz clínico
        edges = [('diabetes', 'glucose'),  # Relación entre diabetes y glucosa
                 ('diabetes', 'blood_pressure')  # Relación entre diabetes y presión sanguínea
                ]
        clinical_model.add_edges_from(edges)
        
        # Añadir CPDs de quiz clínico
        # CPD glucosa en sangre    
        cpd_glucose = TabularCPD(
            variable='glucose', 
            variable_card=3, 
            values=[
                [0.7, 0.3],  # P(glucose=0 | diabetes=0) y P(glucose=0 | diabetes=1)
                [0.2, 0.4],  # P(glucose=1 | diabetes=0) y P(glucose=1 | diabetes=1)
                [0.1, 0.3]   # P(glucose=2 | diabetes=0) y P(glucose=2 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        # CPD para presión sanguínea
        cpd_blood_pressure = TabularCPD(
            variable='blood_pressure', 
            variable_card=2, 
            values=[
                [0.7, 0.4],  # P(bp=0 | diabetes=0) y P(bp=0 | diabetes=1)
                [0.3, 0.6],  # P(bp=1 | diabetes=0) y P(bp=1 | diabetes=1)
            ],
            evidence=['diabetes'], 
            evidence_card=[2]
        )

        # Añadir nuevas CPDs al modelo
        clinical_model.add_cpds(
                cpd_glucose, cpd_blood_pressure
        )
        
        # Comprobar modelo
        assert clinical_model.check_model()

        return clinical_model # Añadir CPDs para las variables adicionales de glucosa y presión sanguínea
        