import math
from datetime import datetime

import pytest
from health_profile import HealthProfile

health_profiles = [
    HealthProfile("Fred Ned", 1984, 186, 95),
    HealthProfile("Basia Kowal", 2000, 165, 52),
    HealthProfile("Jack Smith", 1999, 178, 75)
]


@pytest.mark.parametrize('profile, expected_age', [(health_profiles[0], datetime.now().year - 1984),
                                                   (health_profiles[1], datetime.now().year - 2000),
                                                   (health_profiles[2], datetime.now().year - 1999)])
def test_get_age(profile, expected_age):
    assert profile.get_age() == expected_age


@pytest.mark.parametrize('profile, expected_min_target_hr, expected_max_target_hr', [
    (health_profiles[0], 115.84, 137.56),
    (health_profiles[1], 126.08, 149.72),
    (health_profiles[2], 125.44, 148.96)
])
def test_get_target_hr(profile, expected_min_target_hr, expected_max_target_hr):
    assert profile.get_target_hr() == (expected_min_target_hr, expected_max_target_hr)


@pytest.mark.parametrize('profile, expected_bmi', [
    (health_profiles[0], 27.46),
    (health_profiles[1], 19.10),
    (health_profiles[2], 23.67)
])
def test_get_bmi(profile, expected_bmi):
    assert profile.get_bmi() == expected_bmi


@pytest.mark.parametrize('profiles_list, expected_mean_age, expected_standard_deviation_age', [
    (health_profiles, 28.67, 57.8)])
def test_calculate_age_stats(profiles_list, expected_mean_age, expected_standard_deviation_age):
    assert HealthProfile.calculate_age_stats(profiles_list) == (expected_mean_age, expected_standard_deviation_age)




