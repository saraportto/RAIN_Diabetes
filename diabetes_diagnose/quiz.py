class Quiz:

    def __init__(self):
        pass


    # Bucle para recoger respuestas de INT
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


    # Bucle para recoger respuestas de FLOAT
    def get_float_input(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número decimal (Recuerde introducirlo con . y no con ,).")


    # Hacer QUIZ INICIAL
    def do_initial_quiz(self):
        conseq_diseases = (
            "*Hipertensión\n *Visión borrosa, cuerpos flotantes en la vista, zonas de visión oscura o pérdida de la capacidad visual\n "
            "*Patologías cardiovasculares\n *Apnea del sueño\n *Afecciones de la piel (Infecciones cutáneas, acantosis pigmentaria, necrobiosis lipoídica)\n"
        )

        ### FACTORES DE RIESGO ###
        age_res = self.get_float_input("\n*******************\n❓ ¿Cuál es su edad? \n 0 = menos de 45 años\n 1 = 45 años o más\n>>RESPUESTA EDAD: ")

        if age_res < 45:
            age = 0
        else:
            age = 1

        weight = self.get_float_input("\n*******************\n❓ ¿Cuál es su peso? (en kg): ")
        height = self.get_float_input("\n*******************\n❓ ¿Cuál es su altura? (en cm): ")
        
        bmi_value = weight / ((height / 100) ** 2)

        # Categorizar el BMI según el valor calculado
        if bmi_value < 25:
            bmi = 0  # Bajo peso / Normal
        elif 25 <= bmi_value < 30:
            bmi = 1  # Sobrepeso
        else:
            bmi = 2  # Obesidad
        

        pancreas_diseases = self.get_int_input("\n*******************\n❓ ¿Ha padecido alguna enfermedad o lesión grave del páncreas?\n 0 = no\n 1 = si\n>>RESPUESTA ENFERMEDADES PÁNCREAS: ", [0, 1])
        family_history = self.get_int_input("\n*******************\n❓ ¿Hay antecedentes de diabetes en su familia (padre/madre)? \n 0 = no\n 1 = si\n>>RESPUESTA ANTECEDENTES: ", [0, 1])

        #### SÍNTOMAS ###
        urinate_freq = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente ganas de orinar? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>RESPUESTA FRECUENCIA ORINAR: ", [0, 1, 2])
        thirst = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente ganas de beber agua? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA FRECUENCIA BEBER: ", [0, 1, 2])
        fatigue = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente fatiga? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA FATIGA: ", [0, 1, 2])
        hunger = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente hambre? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA HAMBRE: ", [0, 1, 2])
        weight_loss = self.get_int_input("\n*******************\n❓ ¿Ha tenido alguna pérdida de peso inexplicada recientente? \n 0 = no\n 1 = si\n>>RESPUESTA PÉRDIDA DE PESO: ", [0, 1])

        print("\n*******************\n❓ ¿Ha padecido recientemente o padece alguna de los siguientes?: ", "\n", conseq_diseases)
        sympt_diseases = self.get_int_input("\n 0 = no\n 1 = si\n>>RESPUESTA ENFERMEDADES: ", [0, 1])

        res = {
            'age': age,
            'bmi': bmi,
            'pancreas_diseases': pancreas_diseases,
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
        glucose_level = self.get_float_input("\n*******************\n💊 ¿Cuánto ha dado la medición de glucosa en sangre? (en mg/dL)\n>>>RESPUESTA GLUCOSA EN SANGRE: ")

        if glucose_level < 100:
            glucose = 0  # Normal
        elif 100 <= glucose_level <= 125:
            glucose = 1  # Prediabetes
        else:
            glucose = 2  # Diabetes


        blood_pressure_level = self.get_float_input("\n*******************\n💊 ¿Cuánto ha dado la medición de presión sanguínea? (en mmHg)\n>>>RESPUESTA PRESIÓN SANGUÍNEA: ")

        # Clasificación de presión sanguínea
        if blood_pressure_level < 120:
            blood_pressure = 0  # Normal
        else:
            blood_pressure = 1  # Hipertensión

       
        res = {
            'glucose': glucose,
            'blood_pressure': blood_pressure
        }
        return res
