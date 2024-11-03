class Quiz:

    def __init__(self):
        pass

    def get_int_input(self, prompt, options):
        while True:
            try:
                value = int(input(prompt))
                if value in options:
                    return value
                else:
                    print(f"Por favor, ingrese un número válido.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")

    def get_float_input(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número decimal (Recuerde introducirlo con . y no con ,).")

    def do_initial_quiz(self):
        conseq_diseases = (
            "*Hipertensión\n *Visión borrosa, cuerpos flotantes en la vista, zonas de visión oscura o pérdida de la capacidad visual\n "
            "*Patologías cardiovasculares\n *Apnea del sueño\n *Afecciones de la piel (Infecciones cutáneas, acantosis pigmentaria, necrobiosis lipoídica)\n"
        )
        meds = (
            "*GLUCOCORTICOIDES*\n (prednisona, prednisolona y metilprednisolona)\n----------\n"
            "*ANTISÉPTICOS*\n (clorpromazina, haloperidol, clozapina, olanzapina, risperidona, quetiapina)\n----------\n"
            "*ANTIRRETROVIRALES*\n (zidovudina, estavudina, didanosina, lamivudina, abacavir, tenofovir, emtricitabina, efavirenz, nevirapina, etravirina, nilpivirina, doravirina, indinavir, ritonavir, nelfinavir, lopinavir/ritonavir, atazanavir/ritonavir, darunavir/ritonavir, raltegravir, dolutegravir, elvitegravir, bictegravir)\n----------\n"
            "*INHIBIDORES DE LOS PUNTOS DE CONTROL INMUTINARIOS*\n (Ipilimumab, pembrolizumab, nivolumab, atezolizumab, avelumab, durvalumab)\n"
        )

        sex = self.get_int_input("\n*******************\n❓ ¿Cuál es su sexo? \n 0 = mujer\n 1 = hombre\n>>RESPUESTA SEXO: ", [0, 1])
        age = self.get_int_input("\n*******************\n❓ ¿Cuál es su edad? \n 0 = 0-19 años\n 1 = 20-39 años\n 2 = 40-64 años\n 3 = 65+ años\n>>RESPUESTA EDAD: ", [0, 1, 2, 3])

        weight = self.get_float_input("\n*******************\n❓ ¿Cuál es su peso? (en kg): ")
        height = self.get_float_input("\n*******************\n❓ ¿Cuál es su altura? (en cm): ")

        bmi = weight / ((height / 100) ** 2) # 0: bajopeso/normal (<25); 1: sobrepeso(25-29.9); 2: obesidad: (+30)

        print("\n*******************\n❓ ¿Ha tomado alguno de los siguientes medicamentos?: \n", meds)
        drugs = self.get_int_input("\n 0 = no\n 1 = si\n>>RESPUESTA MEDICAMENTOS: ", [0, 1])

        pancreas_diseases = self.get_int_input("\n*******************\n❓ ¿Ha padecido alguna enfermedad del páncreas?\n 0 = no\n 1 = si\n>>RESPUESTA ENFERMEDADES PÁNCREAS: ", [0, 1])
        pancreas_injury = self.get_int_input("\n*******************\n❓ ¿Ha padecido alguna lesión grave en el páncreas? \n 0 = no\n 1 = si\n>>RESPUESTA LESIÓN: ", [0, 1])
        pregnancies = self.get_int_input("\n*******************\n❓ ¿Ha tenido 3 o más embarazos? \n 0 = no\n 1 = si\n>>RESPUESTA EMBARAZOS: ", [0, 1])
        family_history = self.get_int_input("\n*******************\n❓ ¿Hay antecedentes de diabetes en su familia? \n 0 = no\n 1 = si\n>>RESPUESTA ANTECEDENTES: ", [0, 1])

        urinate_freq = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente ganas de orinar? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>RESPUESTA FRECUENCIA ORINAR: ", [0, 1])
        thirst = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente ganas de beber agua? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA FRECUENCIA BEBER: ", [0, 1])
        fatigue = self.get_int_input("\n*******************\n❓ ¿on qué frecuencia siente fatiga? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA FATIGA: ", [0, 1])
        hunger = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente hambre? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA HAMBRE: ", [0, 1])
        weight_loss = self.get_int_input("\n*******************\n❓ ¿Ha tenido alguna pérdida de peso inexplicada? \n 0 = no\n 1 = si\n>>RESPUESTA PÉRDIDA DE PESO: ", [0, 1])

        print("\n*******************\n❓ ¿Ha padecido recientemente o padece alguna de las siguientes enfermedades?: ", "\n", conseq_diseases)
        sympt_diseases = self.get_int_input("\n 0 = no\n 1 = si\n>>RESPUESTA ENFERMEDADES: ", [0, 1])

        res = {
            'sex': sex,
            'age': age,
            'bmi': bmi,
            'drugs': drugs,
            'pancreas_diseases': pancreas_diseases,
            'pancreas_injury': pancreas_injury,
            'pregnancies': pregnancies,
            'family_history': family_history,
            'urinate_freq': urinate_freq,
            'thirst': thirst,
            'fatigue': fatigue,
            'hunger': hunger,
            'weight_loss': weight_loss,
            'sympt_diseases': sympt_diseases
        }
        return res

    def do_clinical_quiz(self, initial_res: dict):
        glucose = self.get_int_input("💊 ¿A? (1 = sí, 0 = no): ", [0, 1])
        blood_pressure = self.get_int_input("💊 ¿A? (1 = sí, 0 = no): ", [0, 1])
        
        res = {
            'glucose': glucose,
            'blood_pressure': blood_pressure
        }
        return res
