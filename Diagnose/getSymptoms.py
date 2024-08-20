from main import diseases

all_symptoms = []

for d in diseases:
    symptoms = d.getSymptoms()
    symptoms_list = symptoms.split(', ')

    for symptom in symptoms_list:
        if symptom not in all_symptoms:
            all_symptoms.append(symptom)
