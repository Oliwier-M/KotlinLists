import unittest
from matchDieaseses import matching_diseases, matching_symptoms, unique_symptoms, add_value_of_unique_symptoms
from main import save_diseases, get_symptoms


class MainTest(unittest.TestCase):

    def setUp(self):
        self.list_of_diseases = save_diseases()

    def test_get_symptoms(self):
        result = get_symptoms(self.list_of_diseases)
        self.assertEqual(result,['body aches', 'chills', 'cough', 'dehydration', 'diarrhea',
            'difficulty in swallowing', 'dry cough', 'enlarged neck lymph nodes', 'fatigue', 'fever',
            'fluid filled blisters', 'headache', 'joint pain', 'loss of appetite', 'malaise', 'mucus in the throat',
            'muscle ache', 'rashes', 'red bumps', 'red eyes', 'runny nose', 'sensitivity to light',
            'shortness of breath', 'sneezing', 'sore throat', 'stuffy nose', 'swollen eyelids', 'vomiting',
            'watery eyes', 'wheezing'])

    def tearDown(self):
        self.list_of_diseases = []


class MatchDiseasesTest(unittest.TestCase):

    def setUp(self):
        self.user_symptoms = ['vomiting', 'rashes', 'shortness of breath']
        self.list_of_diseases = save_diseases()

        self.unique_sym = ['body aches', 'chills', 'dehydration', 'difficulty in swallowing', 'dry cough'
            , 'fluid filled blisters', 'joint pain', 'mucus in the throat', 'red bumps', 'sensitivity to light'
            , 'shortness of breath', 'swollen eyelids', 'wheezing']

        self.matching_sym = [['smallpox', ['rashes', 'vomiting'], 2]
            , ['pertussis (whooping cough)', ['shortness of breath', 'vomiting'], 2], ['rubella', ['rashes'], 1]
            , ['chickenpox', ['rashes'], 1], ['measles', ['rashes'], 1], ['flu (influenza)', ['vomiting'], 1],
                             ['rotavirus', ['vomiting'], 1]]

    def test_matching_diseases(self):
        result = matching_diseases(self.user_symptoms, self.list_of_diseases)
        self.assertEqual(result, [['pertussis (whooping cough)', ['shortness of breath', 'vomiting'], 2, 1],
                                  ['smallpox', ['rashes', 'vomiting'], 2, 0]])

    def test_matching_symptoms(self):
        result = matching_symptoms(self.user_symptoms, self.list_of_diseases)
        self.assertEqual(result, self.matching_sym)

    def test_unique_symptoms(self):
        result = unique_symptoms(self.list_of_diseases)
        self.assertEqual(result, self.unique_sym)

    def test_add_value_of_unique_symptoms(self):
        result = add_value_of_unique_symptoms(self.matching_sym, self.unique_sym)
        self.assertEqual(result, [['smallpox', ['rashes', 'vomiting'], 2, 0], ['pertussis (whooping cough)',
                                                                               ['shortness of breath', 'vomiting'], 2,
                                                                               1], ['rubella', ['rashes'], 1, 0],
                                  ['chickenpox', ['rashes'], 1, 0], ['measles', ['rashes'], 1, 0],
                                  ['flu (influenza)', ['vomiting'], 1, 0], ['rotavirus', ['vomiting'], 1, 0]])

    def tearDown(self):
        self.user_symptoms = []
        self.list_of_diseases = []


if __name__ == '__main__':
    unittest.main()
