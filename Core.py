import pandas as pd
import xlrd
from Constants import PE_PRR_Dict, ABC_codes_array



class Requirement:

    def __init__(self, row_values):
        self.year = "2022"
        self.PMA = self.set_pma(row_values[8])
        self.PE = self.set_pe(row_values[8])
        self.funding_profile = row_values[5]
        self.type = "CORE"
        self.WUC = "Undefined"
        self.product_category = self.set_product_category(row_values[12])
        self.product = "Undefined"
        self.task_description = row_values[38]
        self.product_count = "Undefined"
        self.location = row_values[17]
        self.org_commercial = "Undefined"
        self.hours = float(row_values[35]) * 1920
        self.work_years = row_values[35]
        self.labor_rate = row_values[34]
        self.labor_cost = float(self.labor_rate) * float(self.work_years)
        self.other_costs = row_values[32]
        self.flat_costs = row_values[33]
        self.total_cost = int(self.labor_cost) + int(self.other_costs) + int(self.flat_costs)


    def set_pma(self, funding_profile):
        for key in PE_PRR_Dict:
            comparison_string = PE_PRR_Dict[key]["STRING"]
            if comparison_string in funding_profile:
                return PE_PRR_Dict[key]["PMA"]
        return "Undefined"

    def set_pe(self, funding_profile):
        for key in PE_PRR_Dict:
            comparison_string = PE_PRR_Dict[key]["STRING"]
            if comparison_string in funding_profile:
                return PE_PRR_Dict[key]["PE"]
        return "Undefined"


    def set_product_category(self, abc_code):
        for array in ABC_codes_array:
            if abc_code in array:
                product_category = array[0]
                return product_category
            elif str(abc_code) == "4.5" or str(abc_code) == "4.7" or str(abc_code) == "6.1":
                return "Product Support/Engineering Support"
            elif str(abc_code) == "4.3":
                return "NAE Activities"
        return abc_code

class Requirements:

    def __init__(self):
        self.years = []
        self.PMAs = []
        self.PEs = []
        self.funding_profiles = []
        self.types = []
        self.WUCs = []
        self.product_categories = []
        self.products = []
        self.task_descriptions = []
        self.product_counts = []
        self.locations = []
        self.org_commercial = []
        self.hours = []
        self.work_years = []
        self.labor_rates = []
        self.labor_costs = []
        self.other_costs = []
        self.flat_costs = []
        self.total_costs = []

    def create_data_frame(self):
        dataframe = pd.DataFrame({
            "Year": self.years,
            "PMA": self.PMAs,
            "PE": self.PEs,
            "Funding Profile": self.funding_profiles,
            "Type": self.types,
            "WUC": self.WUCs,
            "Product Category": self.product_categories,
            "Product": self.products,
            "Task Description": self.task_descriptions,
            "Product Counts": self.product_counts,
            "Location": self.locations,
            "Org or Commercial": self.org_commercial,
            "Hours": self.hours,
            "Work Years": self.work_years,
            "Labor Rate": self.labor_rates,
            "Labor Costs": self.labor_costs,
            "Other Costs": self.other_costs,
            "Flat Rate Costs": self.flat_costs,
            "Total Costs": self.total_costs
        })

        return dataframe

    def add_requirement(self, requirement):
        self.years.append(requirement.year)
        self.PMAs.append(requirement.PMA)
        self.PEs.append(requirement.PE)
        self.funding_profiles.append(requirement.funding_profile)
        self.types.append(requirement.type)
        self.WUCs.append(requirement.WUC)
        self.product_categories.append(requirement.product_category)
        self.products.append(requirement.product)
        self.task_descriptions.append(requirement.task_description)
        self.product_counts.append(requirement.product_count)
        self.locations.append(requirement.location)
        self.org_commercial.append(requirement.org_commercial)
        self.hours.append(requirement.hours)
        self.work_years.append(requirement.work_years)
        self.labor_rates.append(requirement.labor_rate)
        self.labor_costs.append(requirement.labor_cost)
        self.other_costs.append(requirement.other_costs)
        self.flat_costs.append(requirement.flat_costs)
        self.total_costs.append(requirement.total_cost)

