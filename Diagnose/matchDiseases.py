from collections import Counter
from operator import itemgetter


def matching_diseases(user_symptoms, list_of_diseases):
    """

    :param user_symptoms:
    :param list_of_diseases:
    :return:
    """
    matched_symptoms = matching_symptoms(user_symptoms, list_of_diseases)
    unique_sym = unique_symptoms(list_of_diseases)
    matched_symptoms_with_unique_symptoms = add_value_of_unique_symptoms(matched_symptoms, unique_sym)

    most_probable_diseases = sorted(matched_symptoms_with_unique_symptoms, key=itemgetter(3, 2),
                                    reverse=True)  # https://docs.python.org/3/howto/sorting.html

    return most_probable_diseases


def matching_symptoms(user_symptoms, list_of_diseases):
    """

    :param user_symptoms:
    :param list_of_diseases:
    :return:
    """
    matching_sym = []
    for disease in list_of_diseases:
        disease_symptoms = disease.symptoms.split(", ")

        set1 = set(disease_symptoms)
        set2 = set(user_symptoms)

        m_symptoms = set1.intersection(set2)
        if m_symptoms == set():
            matching_sym.append("N/A")
        else:
            matching_sym.append([disease.name, list(m_symptoms), len(list(m_symptoms))])  # the 0 is for counting
            # how many unique symptoms there are

    return matching_sym


def add_value_of_unique_symptoms(matching_symp, unique_sym):
    """

    :param matching_symp:
    :param unique_sym:
    :return:
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
    """

    :param list_of_diseases:
    :return:
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

    return u_symptoms
