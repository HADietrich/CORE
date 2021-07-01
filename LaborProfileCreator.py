import pandas as pd
import xlrd

class LaborProfile:
    def __init__(self, row_values, profile_id):
        self.id = profile_id
        self.year = row_values[0]
        self.funded_activity = row_values[16]
        self.performing_activity = row_values[17]
        self.profile_name = row_values[18]
        self.labor_rate = row_values[34]

    def set_other_cost_profile(self):
        self.id = 1
        self.year = "2022"
        self.funded_activity = "Various"
        self.performing_activity = "Various"
        self.profile_name = "OtherCosts"
        self.labor_rate = 0



class LaborProfiles:
    def __init__(self):
        self.years = ["2022"]
        self.performing_activities = ["Various"]
        self.funded_activities = ["Various"]
        self.labor_rates = [0]
        self.profile_names = ["OtherCosts"]
        self.profile_ids = [1]
        self.composite_keys = []
        self.types = ["N/A"]
        self.profiles = []

    def add_labor_profile(self, labor_profile):
        self.years.append(labor_profile.year)
        self.performing_activities.append(labor_profile.performing_activity)
        self.funded_activities.append(labor_profile.funded_activity)
        self.labor_rates.append(labor_profile.labor_rate)
        self.profile_names.append(labor_profile.profile_name)
        self.profile_ids.append(labor_profile.id)
        self.composite_keys.append(str(labor_profile.funded_activity) + str(labor_profile.profile_name))
        self.types.append("CIV")
        self.profiles.append(labor_profile)
        return

    def check_for_existing(self, composite_key):
        if composite_key in self.composite_keys:
            return True
        else:
            return False

    def find_profile(self, composite_key):

        index_key = self.composite_keys.index(composite_key)
        profile = self.profiles[index_key]

        return profile

    def create_data_frame(self):
        dataframe = pd.DataFrame({
            "ProfileID": self.profile_ids,
            "ProfileName": self.profile_names,
            "FundedActivity": self.funded_activities,
            "PerformingActivity": self.performing_activities,
            "LaborRate": self.labor_rates
        })
        return dataframe




