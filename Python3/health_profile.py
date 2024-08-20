import datetime
import math

class HealthProfile:

    def __init__(self,name,dob,height,weight):
        self.name = name
        self.dob = dob
        self.height = height
        self.weight = weight

    def get_age(self,dob):
        currentYear = datetime.datetime.now().year
        age = currentYear - self.dob
        return age

    def get_targer_hr(self):
        optimalHR = 220 - self.get_age(self.dob)
        minHR = optimalHR * 0.64
        maxHR = optimalHR * 0.76
        return minHR,maxHR

    def get_bmi(self,height,weight):
        BMI = self.weight/math.pow(self.height,2)
        return BMI

    @staticmethod
    def calculate_age_stats(healthProfiles):
        ages = 0
        for profile in healthProfiles:
            ages += profile.get_Age

        meanAge = ages/len(healthProfiles)

# count sum
        powSum = 0
        for profile in healthProfiles:
            powSum += pow((profile.get_Age - ages),2)

        standardDeviationAge = math.sqrt(powSum/len(healthProfiles))

        return meanAge, standardDeviationAge

    @staticmethod
    def find_people_at_risk(healthProfiles):
        peopleAtRisk = []

        for profile in healthProfiles:
            if profile.get_bmi <= 18.5 or 24.9 <= profile.get_bmi:
                peopleAtRisk += profile.name

        return peopleAtRisk


healthProfiles = [
    HealthProfile("Fred Ned",1984,186,95),
    HealthProfile("Basia Kowal",2000,165,52),
    HealthProfile("Jack Smith", 1999,178,75)]








