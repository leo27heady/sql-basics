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
        patient_id=None,
        passport_id=None,
        hemoglobin_level=None,
        glucose_level=None,
        blood_test_time=None,
    ):
        self.patient_id = patient_id
        self.passport_id = passport_id
        self.blood_test_time = blood_test_time
        self.hemoglobin_level = hemoglobin_level
        self.glucose_level = glucose_level


class Covid_analysis:
    def __init__(
        self, covid_result=None, patient_id=None, covid_test_time=None
    ):
        self.covid_result = covid_result
        self.patient_id = patient_id
        self.covid_test_time = covid_test_time
