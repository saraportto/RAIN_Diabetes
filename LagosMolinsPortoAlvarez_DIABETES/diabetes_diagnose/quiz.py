class Quiz:

    # Bucle para recoger respuestas de INT (evita errores)
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


    # Bucle para recoger respuestas de FLOAT (evita errores)
    def get_float_input(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número decimal distinto de 0 (Recuerde introducirlo con . y no con ,).")


    # Hacer QUIZ INICIAL
    def do_initial_quiz(self):
        conseq_diseases = (
            "*Visión borrosa, cuerpos flotantes en la vista, zonas de visión oscura o pérdida de la capacidad visual\n "
            "*Patologías cardiovasculares\n *Apnea del sueño\n *Afecciones de la piel (Infecciones cutáneas, acantosis pigmentaria, necrobiosis lipoídica)\n"
        )

        ### FACTORES DE RIESGO ###
        age_res = self.get_float_input("\n*******************\n❓ ¿Cuál es su edad?\n>>RESPUESTA EDAD: ")

        if age_res < 45:
            age = 0
        else:
            age = 1

        weight = self.get_float_input("\n*******************\n❓ ¿Cuál es su peso? (en kg): ")

        # Compprobación para que la altura no sea 0
        while True:
            height = self.get_float_input("\n*******************\n❓ ¿Cuál es su altura? (en cm): ")
            if height > 0:
                break
            print("La altura no puede ser 0. Por favor, introduzca un valor válido.")        
        
        bmi_value = weight / ((height / 100) ** 2)

        print(f"\n*******************\n\nSu IMC es de {bmi_value:.2f}")

        # Categorizar el BMI según el valor calculado
        if bmi_value < 25:
            bmi = 0  # bajopeso/normal
        elif 25 <= bmi_value < 30:
            bmi = 1  # sobrepeso
        else:
            bmi = 2  # obesidad
        
        pancreas_diseases = self.get_int_input("\n*******************\n❓ ¿Ha padecido alguna enfermedad o lesión grave del páncreas?\n 0 = no\n 1 = si\n>>RESPUESTA ENFERMEDADES PÁNCREAS: ", [0, 1])
        family_history = self.get_int_input("\n*******************\n❓ ¿Hay antecedentes de diabetes en su familia (padre/madre)? \n 0 = no\n 1 = si\n>>RESPUESTA ANTECEDENTES: ", [0, 1])


        #### SÍNTOMAS ###
        urinate_freq = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente ganas de orinar? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>RESPUESTA FRECUENCIA ORINAR: ", [0, 1, 2])
        thirst = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente ganas de beber agua? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA FRECUENCIA BEBER: ", [0, 1, 2])
        fatigue = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente fatiga? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA FATIGA: ", [0, 1, 2])
        hunger = self.get_int_input("\n*******************\n❓ ¿Con qué frecuencia siente hambre? \n 0 = frecuencia baja\n 1 = frecuencia normal\n 2 = frecuencia alta\n>>>RESPUESTA HAMBRE: ", [0, 1, 2])
        weight_loss = self.get_int_input("\n*******************\n❓ ¿Ha tenido alguna pérdida de peso inexplicada recientemente? \n 0 = no\n 1 = si\n>>RESPUESTA PÉRDIDA DE PESO: ", [0, 1])

        print("\n*******************\n❓ ¿Ha padecido recientemente o padece alguna de los siguientes?: ", "\n", conseq_diseases)
        sympt_diseases = self.get_int_input("\n 0 = no\n 1 = si\n>>RESPUESTA ENFERMEDADES: ", [0, 1])

        ### RESPUESTAS del quiz ###
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

    # Hacer QUIZ CLÍNICO
    def do_clinical_quiz(self):

        ### Glucosa
        glucose_level = self.get_float_input("\n*******************\n💊 ¿Cuál es su nivel de glucosa en sangre en la medición realizada? (en mg/dL)\n>>>RESPUESTA GLUCOSA EN SANGRE: ")

        # Categoriza nivel de glucosa
        if glucose_level < 100:
            glucose = 0  # normal
        elif 100 <= glucose_level < 125:
            glucose = 1  # prediabetes
        else:
            glucose = 2  # diabetes


        ### Presión sanguínea
        systolic = self.get_float_input("\n*******************\n💊 ¿Cuál ha sido su medición de presión sistólica (número superior)? (en mmHg): ")
        diastolic = self.get_float_input("\n💊 ¿Cuál ha sido su medición de presión diastólica (número inferior)? (en mmHg): ")

        # Clasificación de presión sanguínea
        if systolic < 130 and diastolic < 80:
            blood_pressure = 0 # normal
        else:
            blood_pressure = 1 # hipertenso


        ### RESPUESTAS del quiz ###
        res = {
            'glucose': glucose,
            'blood_pressure': blood_pressure
        }
        
        return res
