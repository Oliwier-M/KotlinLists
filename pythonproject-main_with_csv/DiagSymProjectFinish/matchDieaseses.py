from collections import Counter
from operator import itemgetter

# to test unit test, create in the test, symptom list disease list, both empty, error cases
def matching_diseases(user_symptoms, list_of_diseases):
    """Creates a sorted by most probable disease list.

    Args:
        user_symptoms: list of strings representing users symptoms
        list_of_diseases: list of disease objects
    Returns:
        List: list of probable or most probable diseases
    """
    matched_symptoms = matching_symptoms(user_symptoms, list_of_diseases)
    unique_sym = unique_symptoms(list_of_diseases)
    matched_symptoms_with_unique_symptoms = add_value_of_unique_symptoms(matched_symptoms, unique_sym)

    most_probable_diseases = sorted(matched_symptoms_with_unique_symptoms, key=itemgetter(3, 2),
                                    reverse=True)  # https://docs.python.org/3/howto/sorting.html

    if len(user_symptoms) > 1:
        probable_diseases = []
        for x in range(len(most_probable_diseases)):
            if most_probable_diseases[x][2] > 1 or most_probable_diseases[x][3] > 0:
                probable_diseases.append(most_probable_diseases[x])
        return probable_diseases
    else:
        return most_probable_diseases


def matching_symptoms(user_symptoms, list_of_diseases):
    """Creates a list of diseases with symptoms which are matching with the ones provided by user.

    Args:
        list of strings representing users symptoms
        list_of_diseases: list of disease objets
    Returns:
        List: list of arrays which contain: disease name, list of symptoms, number of matching symptoms
    """
    matching_sym = []
    for disease in list_of_diseases:
        disease_symptoms = disease.symptoms.split(", ")

        set1 = set(disease_symptoms)
        set2 = set(user_symptoms)

        m_symptoms = set1.intersection(set2)
        if m_symptoms == set():
            continue
        else:
            matching_sym.append([disease.name, sorted(list(m_symptoms)), len(list(m_symptoms))])

    return matching_sym


def add_value_of_unique_symptoms(matching_symp, unique_sym):
    """Checks how many of matching symptoms are unique and adds their to the matching_sym list.

    Args:
        matching_symp: list of diseases that have symptoms which match user symptoms
        unique_sym: list of unique symptoms
    Returns:
        List: updated matching_symp with number(integer) of unique symptoms occurring in the matching_sym
    """
    counter = 0
    for i in range(len(matching_symp)):
        name, symptoms, amount_of_symptoms = matching_symp[i]
        for symptom in symptoms:
            if symptom in unique_sym:
                counter += 1
        matching_symp[i].append(counter)
        counter = 0

    return matching_symp


def unique_symptoms(list_of_diseases):
    """Creates list only of unique symptoms.

    Args:
        list_of_diseases: list of disease objects

    Returns:
        List: list of unique symptoms as strings
    """
    all_symptoms = []
    u_symptoms = []

    for disease in list_of_diseases:
        disease_symptoms = disease.symptoms.split(", ")
        for sym in disease_symptoms:
            all_symptoms.append(sym)

    all_symptoms_counter = Counter(all_symptoms)  # https://docs.python.org/3/library/collections.html

    for symptom, count in all_symptoms_counter.items():
        if count == 1:
            u_symptoms.append(symptom)

    return sorted(u_symptoms)
