from disease import Disease
import csv


def save_diseases():
    """Reads the csv file and saves its parameters into a list of objects of type Disease, created in a previous file.
    
    Returns:
        List: list of Disease objects
    """
    with open("InfectiousDiseases.csv") as f:
        content = csv.reader(f, delimiter=';')

        diseases = []

        for row in content:
            d = Disease(row[0], row[1], row[2], row[3], row[4])
            diseases.append(d)

    return diseases


def get_symptoms(diseases):
    """Generates a list of all symptoms that appear in the "diseases" list of objects <Disease>.
    
    Args:
        diseases: a list of objects of type Disease
    Returns: 
        List: list<String> of all symptoms that appear in the csv file, without
    """
    all_symptoms = []

    for d in diseases:
        symptoms = d.symptoms
        symptoms_list = symptoms.split(', ')

        for symptom in symptoms_list:
            if symptom not in all_symptoms:
                all_symptoms.append(symptom)

    return sorted(all_symptoms)
