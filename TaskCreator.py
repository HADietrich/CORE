import xlrd
import pandas as pd
from Constants import ABC_codes_array


class Task:
    def __init__(self, row_value, task_id):
        self.task_id = task_id
        self.funding_element_name = row_value[15]
        self.year = "2022"
        self.pma = self.set_pma(row_value[5])
        self.pe = self.set_pe(row_value[5])
        self.funding_profile = row_value[5]
        self.type = "CORE"
        self.WUC = "WUC"
        self.product_category = self.set_product_category(row_value[12])
        self.product = "Product"
        self.task_description = row_value[38]
        self.product_count = 0

    def set_pma(self, funding_profile):
        if "F18E F PRL" in funding_profile or "F414 ENG PRL" in funding_profile:
            pma = "265"
        elif "CMV22 PRL" in funding_profile:
            pma = "275"
        elif "V22 PRL" in funding_profile:
            pma = "275"
        elif "H60 PRL" in funding_profile or "T700 ENG PRL" in funding_profile:
            pma = "299"
        else:
            pma = "Undefined"
        return pma

    def set_pe(self, funding_profile):
        if "F18E F PRL" in funding_profile or "F414 ENG PRL" in funding_profile:
            program_element = "0204136N"
        elif "CMV22 PRL" in funding_profile:
            program_element = "0204151N"
        elif "V22 PRL" in funding_profile:
            program_element = "0206121M"
        elif "H60 PRL" in funding_profile or "T700 ENG PRL" in funding_profile:
            program_element = "0204243N"
        else:
            program_element = "Undefined"
        return program_element

    def set_product_category(self, abc_code):
        for array in ABC_codes_array:
            if abc_code in array:
                product_category = array[0]
                return product_category
        return abc_code

class Tasks:
    def __init__(self):
        self.task_ids = []
        self.funding_element_names = []
        self.years = []
        self.pmas = []
        self.pes = []
        self.funding_profiles = []
        self.types = []
        self.WUCS = []
        self.product_categories = []
        self.products = []
        self.task_descriptions = []
        self.product_counts = []

    def add_task(self, task):
        self.task_ids.append(task.task_id)
        self.funding_element_names.append(task.funding_element_name)
        self.years.append(task.year)
        self.pmas.append(task.pma)
        self.pes.append(task.pe)
        self.funding_profiles.append(task.funding_profile)
        self.types.append(task.type)
        self.WUCS.append(task.WUC)
        self.product_categories.append(task.product_category)
        self.products.append(task.product)
        self.product_counts.append(task.product_count)
        self.task_descriptions.append(task.task_description)

        return

    def check_for_existing(self, fe_name):
        if fe_name in self.funding_element_names:
            return True
        else:
            return False

    def create_data_frame(self):
        dataframe = pd.DataFrame({
            "TaskID": self.task_ids,
            "FundingElementName": self.funding_element_names,
            "Year": self.years,
            "PMA": self.pmas,
            "PE": self.pes,
            "FundingProfile": self.funding_profiles,
            "Type": self.types,
            "WUC": self.WUCS,
            "ProductCategory": self.product_categories,
            "Product": self.products,
            "ProductCount": self.product_counts,
            "TaskDescription": self.task_descriptions,
        })

        return dataframe
