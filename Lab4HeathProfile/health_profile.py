import datetime
import math

class HealthProfile:

    def __init__(self, name, dob, height, weight):
        self.name = name
        self.dob = dob
        self.height = height
        self.weight = weight

    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.dob
        return age

    def get_target_hr(self):
        optimal_hr = 220 - self.get_age()
        min_hr = optimal_hr * 0.64
        max_hr = optimal_hr * 0.76
        return min_hr, max_hr

    def get_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / math.pow(height_in_meters, 2)
        bmi = round(bmi, 2)
        return bmi

    @staticmethod
    def calculate_age_stats(healthProfiles):
        ages = 0
        for profile in healthProfiles:
            ages += profile.get_age()

        mean_age = ages / len(healthProfiles)
        mean_age = round(mean_age,2)

        # count sum
        pow_sum = 0
        for profile in healthProfiles:
            pow_sum += pow((profile.get_age() - ages), 2)

        standard_deviation_age = math.sqrt(pow_sum / len(healthProfiles))
        standard_deviation_age = round(standard_deviation_age,2)

        return mean_age, standard_deviation_age

    @staticmethod
    def find_people_at_risk(list_of_health_profiles):
        people_at_risk = []

        for patient in list_of_health_profiles:
            bmi = patient.get_bmi()
            if bmi <= 18.5 or 24.9 <= bmi:
                people_at_risk.append(patient.name)

        return people_at_risk


if __name__ == '__main__':
    health_profiles = [
        HealthProfile("Fred Ned", 1984, 186, 95),
        HealthProfile("Basia Kowal", 2000, 165, 52),
        HealthProfile("Jack Smith", 1999, 178, 75)]

    for profile in health_profiles:
        print("Name: " + profile.name)
        print("AGE: " + str(profile.get_age()))
        print("MINIMUM HEART RATE: " + str(profile.get_target_hr()[0]))
        print("MAXIMUM HEART RATE: " + str(profile.get_target_hr()[1]))
        print("BMI: " + str(profile.get_bmi()))
        print()  # just skipping a line

    age_stats = HealthProfile.calculate_age_stats(health_profiles)
    print("MEAN OF AGE: " + str(age_stats[0]))
    print("STANDARD DEVIATION OF AGE: " + str(age_stats[1]))


    patients_at_risk = HealthProfile.find_people_at_risk(health_profiles)
    patients_at_risk = ''.join(patients_at_risk)
    print("Patients at risk: " + patients_at_risk)

