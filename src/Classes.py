class Patient:
    def __init__(
        self, passport_id=None, full_name=None, birthday=None, sex=None
    ):
        self.passport_id = passport_id
        self.full_name = full_name
        self.birthday = birthday
        self.sex = sex


class Blood_test:
    def __init__(
        self,
        hemoglobin_level=None,
        glucose_level=None,
        blood_test_time=None,
    ):
        self.blood_test_time = blood_test_time
        self.hemoglobin_level = hemoglobin_level
        self.glucose_level = glucose_level


class Covid_analysis:
    def __init__(self, covid_result=None, covid_test_time=None):
        self.covid_result = covid_result
        self.covid_test_time = covid_test_time
